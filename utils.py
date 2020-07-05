# -*- coding: utf-8 -*-

import logging
import os
import pandas as pd
import PyPDF2


class PdfMerge:
    def __init__(self):
        formatter = logging.Formatter('%(asctime)s [%(threadName)s] %(levelname)s: %(message)s')
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        sh.setLevel(logging.DEBUG)
        self.logger = logging.getLogger(__file__)
        self.logger.addHandler(sh)
        self.logger.setLevel(logging.DEBUG)

    def save_file_name(self, dir_path, encoding='gbk'):
        """
        获取文件夹dir下PDF文件的名称，并保存到CSV文件中
        :param dir_path: 文件夹路径
        :param encoding: 文件编码
        :return:
        """
        index = ['学号']
        student_number = []
        all_files_name = os.listdir(dir_path)  # 读取文件夹下的所有文件名
        for file_name in all_files_name:
            if file_name.endswith('.pdf'):  # 判断是否为PDF文件名
                file_name = file_name[:-6]  # 1800271038-1.pdf ——> 1800271038
                if file_name not in student_number:  # 存在1800271038-1.pdf，1800271038-2.pdf的情况
                    student_number.append(file_name)
        csv_file = pd.DataFrame(columns=index, data=student_number)  # 把list保存成CSV文件
        csv_file.to_csv('./student_number.csv', encoding=encoding)

    def get_file_name(self, file_dir_path, encoding='gbk'):
        """
        读取CSV文件中的PDF文件名，并保存到list中
        :param file_dir_path: CSV文件的路径
        :param encoding: 文件编码
        :return: PDF文件名
        """
        all_files_name = []
        csv_data = pd.read_csv(file_dir_path, encoding=encoding)  # 读取CSV文件
        files_name_list = csv_data.values.tolist()  # 转成list
        for file in files_name_list:
            file_name = str(file[-1])  # 返回PDF文件名，并转成字符串
            all_files_name.append(file_name)
        return all_files_name

    def merge_pdf_file(self, file_dir_path, file_name, save_dir_path='', file_format='.pdf', encoding='gbk'):
        """
        根据项目需求，合并两个PDF文件
        :param file_dir_path: 两个PDF文件的文件夹路径
        :param file_name: PDF文件名的前缀
        :param save_dir_path: 合并后PDF的保存路径
        :param file_format: 文件格式
        :return:
        """
        if not save_dir_path:
            save_dir_path = file_dir_path
        file1_name = file_name + '-1' + file_format  # PDF1的文件名
        file2_name = file_name + '-2' + file_format  # PDF2的文件名
        file1_absolute_path = os.path.join(file_dir_path, file1_name)  # PDF1的绝对路径
        file2_absolute_path = os.path.join(file_dir_path, file2_name)  # PDF2的绝对路径

        pdfWriter = PyPDF2.PdfFileWriter()
        # with open(file1_absolute_path, 'rb') as pdfFileObj1, open(file2_absolute_path, 'rb') as pdfFileObj2:
        pdfFileObj1 = open(file1_absolute_path, 'rb')
        pdfFileObj2 = open(file2_absolute_path, 'rb')

        pdfReader1 = PyPDF2.PdfFileReader(pdfFileObj1)
        pdfReader2 = PyPDF2.PdfFileReader(pdfFileObj2)

        # 如果pdf文件已经加密，必须首先解密才能使用pyPdf
        if pdfReader1.isEncrypted == True:
            pdfReader1.decrypt("map")
        if pdfReader2.isEncrypted == True:
            pdfReader2.decrypt("map")

        if pdfReader1.numPages != pdfReader2.numPages:
            self.logger.error(f'The numPages({pdfReader1.numPages}) of {file1_name} is not equal '
                              f'to that({pdfReader2.numPages}) of {file2_name}.')
            return None
        # 合并pdf
        for pageIndex in zip(range(pdfReader1.numPages), range(pdfReader2.numPages-1, -1, -1)):
            page1 = pdfReader1.getPage(pageIndex[0])
            page2 = pdfReader2.getPage(pageIndex[1])
            pdfWriter.addPage(page1)
            pdfWriter.addPage(page2)


        # 保存合并后的pdf
        pdfOutput_name = file_name + file_format  # PDF的文件名
        pdfOutput_absolute_path = os.path.join(save_dir_path, pdfOutput_name)  # PDF的绝对路径
        print(pdfOutput_absolute_path)
        pdfOutput = open(pdfOutput_absolute_path, "wb")
        pdfWriter.write(pdfOutput)
        pdfOutput.close()
        pdfFileObj1.close()
        pdfFileObj2.close()
            # with open(pdfOutput_absolute_path, 'wb') as pdfOutput:
            #     pdfWriter.write(pdfOutput)
            #     print(pdfOutput_absolute_path)


if __name__ == '__main__':
    dirPath = r"E:\IoT\MaoningGuan\学位论文\test1"  # 扫描件的路径
    save_path = r'E:\IoT\MaoningGuan\学位论文\test2'  # 合并后保存的路径
    file_path = r'./student_number.csv'  # 保存pdf文件名的CSV文件的路径

    pdfMerge = PdfMerge()
    pdfMerge.save_file_name(dirPath)
    files_name = pdfMerge.get_file_name(file_path)  # 获取文件名
    for file_name in files_name:
        pdfMerge.merge_pdf_file(dirPath, file_name, save_path)  # 合并PDF文件
    # print(csv_data.shape)
    # for line in csv_data[list(range(3, 6))]:
    #     print(line)
