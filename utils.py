# -*- coding: utf-8 -*-

import fitz
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

    def merge_pdf_file(self, file_dir_path, file_name, save_dir_path='', file_format='.pdf'):
        """
        根据项目需求，合并两个扫描的PDF文件（合并可编辑的PDF也适用）
        :param file_dir_path: 两个PDF文件的文件夹路径
        :param file_name: PDF文件名的前缀
        :param save_dir_path: 合并后PDF的保存路径
        :param file_format: 文件格式
        :return:
        """
        if not save_dir_path:
            save_dir_path = file_dir_path

        if not os.path.exists(save_dir_path):  # 判断存放文件夹是否存在
            os.makedirs(save_dir_path)  # 若文件夹不存在就创建

        doc = fitz.open()

        file1_name = file_name + '-1' + file_format  # PDF1的文件名
        file2_name = file_name + '-2' + file_format  # PDF2的文件名
        file1_absolute_path = os.path.join(file_dir_path, file1_name)  # PDF1的绝对路径
        file2_absolute_path = os.path.join(file_dir_path, file2_name)  # PDF2的绝对路径
        pdfDoc1 = fitz.open(file1_absolute_path)
        pdfDoc2 = fitz.open(file2_absolute_path)
        if pdfDoc1.pageCount != pdfDoc2.pageCount:
            self.logger.error(f'The numPages({pdfDoc1.pageCount}) of {file1_name} is not equal '
                              f'to that({pdfDoc2.pageCount}) of {file2_name}.')
            return None

        for pageIndex in zip(range(pdfDoc1.pageCount), range(pdfDoc2.pageCount - 1, -1, -1)):
            page1 = pageIndex[0]
            page2 = pageIndex[1]
            doc.insertPDF(pdfDoc1, from_page=page1, to_page=page1)  # 将当前页插入文档
            doc.insertPDF(pdfDoc2, from_page=page2, to_page=page2)  # 将当前页插入文档

        # 保存合并后的pdf
        pdfOutput_name = file_name + file_format  # PDF的文件名
        pdfOutput_absolute_path = os.path.join(save_dir_path, pdfOutput_name)  # PDF的绝对路径
        if os.path.exists(pdfOutput_absolute_path):
            os.remove(pdfOutput_absolute_path)
        doc.save(pdfOutput_absolute_path)
        doc.close()
        pdfDoc1.close()
        pdfDoc2.close()


if __name__ == '__main__':
    dirPath = r"E:\Python\code\universalCode\pdf-merging\test1"  # 扫描件的路径
    save_path = r'E:\Python\code\universalCode\pdf-merging\test2'  # 合并后保存的路径
    file_path = r'./student_number.csv'  # 保存pdf文件名的CSV文件的路径

    pdfMerge = PdfMerge()
    pdfMerge.save_file_name(dirPath)
    files_name = pdfMerge.get_file_name(file_path)  # 获取文件名
    for file_name in files_name:
        pdfMerge.merge_pdf_file(dirPath, file_name, save_path)  # 合并PDF文件

