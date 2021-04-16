#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mysqloperation.py
@Date    :   2021/04/16 20:36
@Author  :   LJH
@Version :   1.0
@License :   MIT License
@Desc    :   None
'''

# ————————————————————————————————————————————————————————————

# 数据库的增删改查

# import pymysql

# database = pymysql.connect(host="localhost",port=3306,user="LJH",passwd="Ljh960919",db="db",charset = "utf8")
# # 初始化指针
# cursor = database.cursor()

# 增
# 格式："INSERT INTO 表名 (字段1,字段2,字段3) VALUES (内容1,内容2,内容3);"
# sql = "INSERT INTO 7月下旬入库表 (date,company,province,price,weight) VALUES ('2019-9-20','河北粮食','河北','2200','45.1');"
# cursor.execute(sql) # 执行sql语句
# database.commit()  # 对存储的数据修改后，需要commit
# database.close()

# 改
# 格式："UPDATE 表名 SET 字段1=内容1,字段2=内容2  WHERE 条件;"

# sql = "UPDATE 7月下旬入库表 SET date='2018-09-21' WHERE date='2019-09-20';"
# cursor.execute(sql)
# database.commit()  # 对存储的数据修改后，需要commit
# database.close()

# 查
# 基础语法："SELECT 字段 FROM 表名 WHERE 条件"
# 查询全部字段用*

# sql = "SELECT company,price*weight FROM 7月下旬入库表 WHERE date='2018-07-21';"
# sql = "SELECT company,sum(weight) FROM 7月下旬入库表 WHERE date='2018-07-21' GROUP BY company;"
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)
# database.close()

# 删
# 格式："DELETE FROM 表名 WHERE 条件;" 条件的写法 ：字段=内容

# sql = "DELETE FROM 7月下旬入库表 WHERE date='2018-09-21';"
# cursor.execute(sql)
# database.commit()  # 对存储的数据修改后，需要commit
# database.close()


# ————————————————————————————————————————————————————————————
# 数据库的提取处理和excel的导出

# import xlrd
# import xlwt
# from xlutils.copy import copy

# cursor = database.cursor()

# sql = "SELECT company ,COUNT(company),SUM(weight),SUM(weight*price) FROM 7月下旬入库表 GROUP BY company"
# cursor.execute(sql)
# result = cursor.fetchall()
# # print(result)
# for i in result:
#     if i[0] == '张三粮配':
#         a_num = i[1]
#         a_weight = i[2]
#         a_total_price = i[3]
#     elif i[0] == '李四粮食':
#         b_num = i[1]
#         b_weight = i[2]
#         b_total_price = i[3]
#     elif i[0] == '王五小麦':
#         c_num = i[1]
#         c_weight = i[2]
#         c_total_price = i[3]
#     elif i[0] == '赵六麦子专营':
#         d_num = i[1]
#         d_weight = i[2]
#         d_total_price = i[3]

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

# new_sheet.write(2, 1, a_num, style)
# new_sheet.write(2, 2, a_weight, style)
# new_sheet.write(2, 3, a_total_price, style)
# new_sheet.write(3, 1, b_num, style)
# new_sheet.write(3, 2, b_weight, style)
# new_sheet.write(3, 3, b_total_price, style)
# new_sheet.write(4, 1, c_num, style)
# new_sheet.write(4, 2, c_weight, style)
# new_sheet.write(4, 3, c_total_price, style)
# new_sheet.write(5, 1, d_num, style)
# new_sheet.write(5, 2, d_weight, style)
# new_sheet.write(5, 3, d_total_price, style)

# new_excel.save(r"D:\Code\自学笔记\练习材料\Python\7月下旬统计表.xls")


# ————————————————————————————————————————————————————————————




# ————————————————————————————————————————————————————————————




# ————————————————————————————————————————————————————————————



