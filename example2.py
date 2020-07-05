# -*- coding: utf-8 -*-
from utils import PdfMerge


def main():
    dirPath = r"E:\IoT\MaoningGuan\学位论文\2018级开题报告扫描原件"  # 扫描件的路径
    save_path = r'E:\IoT\MaoningGuan\学位论文\2018级开题报告扫描合成版'  # 合并后保存的路径
    file_path = r'./student_number.csv'  # 保存pdf文件名的CSV文件的路径

    pdfMerge = PdfMerge()
    pdfMerge.save_file_name(dirPath)
    files_name = pdfMerge.get_file_name(file_path)  # 获取文件名
    for file_name in files_name:
        print(file_name)
        pdfMerge.merge_pdf_file(dirPath, file_name, save_path)  # 合并PDF文件


if __name__ == '__main__':
    main()