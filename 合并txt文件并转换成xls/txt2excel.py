#!/usr/bin/python
# -*- coding: utf-8 -*-

import os  
import sys  
import xlwt

def txt2excel(txtFile, excelFile):
	print("Converting xls...")
	f = open(txtFile)
	x = 0 # 行
	y = 0 # 列
	xls = xlwt.Workbook() # 生成一个excel文件
	sheet = xls.add_sheet('sheet1', cell_overwrite_ok=True) # 生成一个sheet
	while True:
		line = f.readline() # 一行一行读取txt文件
		if not line: # 如果此行为空，则跳出
			break
		for i in line.split('**'): # txt文件每列用**分隔，当让也可以用其他符号分隔
			item = i.strip()
			sheet.write(x, y, item) # 将item写入第一行第一列
			y = y + 1 
		x = x + 1
		y = 0 # 下一个循环又从第一列开始
	f.close()
	xls.save(excelFile + '.xls')

if __name__ == "__main__":
	txtFile = sys.argv[1]
	excelFile = sys.argv[2]
	txt2excel(txtFile, excelFile)