# -*- coding: utf-8 -*-
"""
使用示例3：
重命名合并后的PDF文件
"""
import logging
import os
import pandas as pd
import shutil
import xlrd

from utils import PdfMerge


formatter = logging.Formatter('%(asctime)s [%(threadName)s] %(levelname)s: %(message)s')
sh = logging.StreamHandler()
sh.setFormatter(formatter)
sh.setLevel(logging.DEBUG)
logger = logging.getLogger(__file__)
logger.addHandler(sh)
logger.setLevel(logging.DEBUG)


def rename_merged_pdf():
    save_path = r'E:\IoT\MaoningGuan\学位论文\2018级开题报告扫描合成版'  # 合并后保存的路径
    new_save_path = r'E:\IoT\MaoningGuan\学位论文\2018级开题报告扫描合成版（重命名）'  # 保存重命名后的文件路径
    file_path = r'./研究生名单2018.xls'
    student_name_pdf = r'./student_name_pdf.csv'
    file_format = '.pdf'

    if not os.path.exists(new_save_path):
        os.mkdir(new_save_path)

    # 获取旧的名字
    old_files_name = os.listdir(save_path)  # 读取文件夹下的所有文件名

    # 获取新的名字
    wb = xlrd.open_workbook(filename=file_path)  # 打开文件
    # print(wb.sheet_names())  # 获取所有表格名字
    sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格
    # print(sheet1.name, sheet1.nrows, sheet1.ncols)
    student_num = sheet1.col_values(0)  # 获取学号
    student_num = student_num[1:]
    name = sheet1.col_values(1)  # 获取姓名
    name = name[1:]

    if len(student_num) != len(name):
        logger.error('The length of  column student number is not equal to that of column name.')
        return None
    new_name_dict = dict(zip(student_num, name))
    # print(new_name_dict)

    # 重命名PDF文件
    # for old_file_name in old_files_name:
    #     old_name = old_file_name.strip(file_format)
    #     student_name = new_name_dict.get(old_name)
    #     if student_name:
    #         new_file_name = old_name + '-' + student_name + file_format  # 拼接新的文件名
    #         # 重命名PDF文件
    #         print(f'重命名：{old_file_name} ——> {new_file_name}')
    #         shutil.copyfile(os.path.join(save_path, old_file_name), os.path.join(new_save_path, new_file_name))
    #     else:
    #         logger.warning(f'The student number {old_name} is not exist.')

    # 保存已合成的PDF的最新名单
    student_name_list = []
    for old_file_name in old_files_name:
        old_name = old_file_name.strip(file_format)
        student_name = new_name_dict.get(old_name)
        if student_name:
            student_name_list.append([old_name, student_name])
        else:
            logger.warning(f'The student number {old_name} is not exist.')
    print(student_name_list)
    index = ['学号', '姓名']
    csv_file = pd.DataFrame(columns=index, data=student_name_list)  # 把list保存成CSV文件
    csv_file.to_csv(student_name_pdf, encoding='gbk')

if __name__ == '__main__':
    rename_merged_pdf()