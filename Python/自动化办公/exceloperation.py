#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   exceloperation.py
@Date    :   2021/04/16 20:37
@Author  :   LJH
@Version :   1.0
@License :   MIT License
@Desc    :   None
'''

# ————————————————————————————————————————————————————————————

# 统计表格数据，并填入模板

# import xlrd
# import xlwt
# from xlutils.copy import copy

# xlsx = xlrd.open_workbook(r"D:\Code\自学笔记\练习材料\Python\7月下旬入库表.xls")

# table = xlsx.sheet_by_index(0)

# all_data = []
# for n in range(1, table.nrows):
#     company = table.cell(n, 1).value
#     price = table.cell(n, 3).value
#     weight = table.cell(n, 4).value

#     data = {'company': company, 'weight': weight, 'price': price}
#     all_data.append(data)
# # 以下内容可以用pandas的groupby轻易实现，这里不引入新知识，使用一个笨办法
# a_weight = []
# a_total_price = []
# b_weight = []
# b_total_price = []
# c_weight = []
# c_total_price = []
# d_weight = []
# d_total_price = []

# for i in all_data:
#     if i['company'] == '张三粮配':
#         a_weight.append(i['weight'])
#         a_total_price.append(i['weight'] * i['price'])
#     if i['company'] == '李四粮食':
#         b_weight.append(i['weight'])
#         b_total_price.append(i['weight'] * i['price'])
#     if i['company'] == '王五小麦':
#         c_weight.append(i['weight'])
#         c_total_price.append(i['weight'] * i['price'])
#     if i['company'] == '赵六麦子专营':
#         d_weight.append(i['weight'])
#         d_total_price.append(i['weight'] * i['price'])


# tem_excel = xlrd.open_workbook(r"D:\Code\自学笔记\练习材料\Python\模板.xls", formatting_info=True)
# tem_sheet = tem_excel.sheet_by_index(0)

# new_excel = copy(tem_excel)
# new_sheet = new_excel.get_sheet(0)

# style = xlwt.XFStyle()

# font = xlwt.Font()
# font.name = '微软雅黑'
# font.bold = True
# font.height = 360
# style.font = font

# borders = xlwt.Borders()
# borders.top = xlwt.Borders.THIN
# borders.bottom = xlwt.Borders.THIN
# borders.left = xlwt.Borders.THIN
# borders.right = xlwt.Borders.THIN
# style.borders = borders

# alignment = xlwt.Alignment()
# alignment.horz = xlwt.Alignment.HORZ_CENTER
# alignment.vert = xlwt.Alignment.VERT_CENTER
# style.alignment = alignment

# new_sheet.write(2, 1, len(a_weight), style)
# new_sheet.write(2, 2, round(sum(a_weight), 2), style)
# new_sheet.write(2, 3, round(sum(a_total_price), 2), style)
# new_sheet.write(3, 1, len(b_weight), style)
# new_sheet.write(3, 2, round(sum(b_weight), 2), style)
# new_sheet.write(3, 3, round(sum(b_total_price), 2), style)
# new_sheet.write(4, 1, len(c_weight), style)
# new_sheet.write(4, 2, round(sum(c_weight), 2), style)
# new_sheet.write(4, 3, round(sum(c_total_price), 2), style)
# new_sheet.write(5, 1, len(d_weight), style)
# new_sheet.write(5, 2, round(sum(d_weight), 2), style)
# new_sheet.write(5, 3, round(sum(d_total_price), 2), style)


# new_excel.save(r"D:\Code\自学笔记\练习材料\Python\7月下旬统计表.xls")


# ————————————————————————————————————————————————————————————
# 用xlsxwriter,openpyxl更灵活地操作Excel

# xlwt  写入xls，超过256列报错

# import xlwt
# workbook = xlwt.Workbook()
# sheet0 = workbook.add_sheet("sheet0")
# for i in range(0,200):
#     sheet0.write(0,i,i)
# workbook.save(r"D:\Code\自学笔记\练习材料\Python\number1.xls")

# xlsxwriter    写入xlsx，不支持带格式文件

# import xlsxwriter as xw
# workbook = xw.Workbook(r"D:\Code\自学笔记\练习材料\Python\number.xlsx")
# sheet0 = workbook.add_worksheet("sheet0")
# for i in range(0,300):
#     sheet0.write(0,i,i)
# workbook.close()

# openpyxl  性能不稳定

# import openpyxl
# workbook = openpyxl.load_workbook(r"D:\Code\自学笔记\练习材料\Python\模板1.xlsx")
# sheet0 = workbook["Sheet1"]
# sheet0['B3'] = "5"
# sheet0['B4'] = "3"
# sheet0['B5'] = 6
# sheet0['B6'] = 7
# workbook.save(r"D:\Code\自学笔记\练习材料\Python\XX公司7月5日入库表.xlsx")


# ————————————————————————————————————————————————————————————
# 快速整理文件名到Excel表

# import os,xlwt

# file_dir = r"D:\Code\自学笔记\练习材料\Python"

# os.listdir(file_dir)
# new_workbook = xlwt.Workbook()
# worksheet = new_workbook.add_sheet("new_test")
# n = 0
# for i in os.listdir(file_dir):
#     worksheet.write(n,0,i)
#     n += 1
# new_workbook.save(r"D:\Code\自学笔记\练习材料\Python\file_name.xls")


# ————————————————————————————————————————————————————————————




# ————————————————————————————————————————————————————————————




# ————————————————————————————————————————————————————————————



