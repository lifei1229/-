# -*- coding:UTF-8 -*-

import xlwt

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1')
worksheet.write(0,0,'hello')
workbook.save('studet.xls')