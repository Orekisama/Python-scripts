#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pymysql # 需要此模块连接mysql
import xlrd # 需要此模块读取xls文件

db_host = 'localhost'
db_port = 3306
db_user = 'root'
db_pw = '123'

def excel2mysql():
	data = xlrd.open_workbook(sys.argv[1]) # 读取xls文件为第一个参数
	table = data.sheets()[1] # 读取xls文件的第一个sheet
	nrows = table.nrows # 行
	ncols = table.ncols # 列

	src_db = pymysql.connect(host=db_host, port=db_port, user=db_user, passwd=db_pw)
	cursor = src_db.cursor()

	for i in range(1, nrows):
		line = table.row_values(i) # 第一次循环获取第一行数据
		cname_1 = line[0]
		did_1 = line[3]
		dmain_1 = line[1]
		bandwidth_1 = line[4]

		insert_sql = 'insert into mysite.ccna_ccna (cname, did, domain, bandwidth) values(%s, %s, %s, %s)'
		cursor.execute(insert_sql, (cname_1, did_1, domain_1, bandwidth_1)) # 批量执行insert语句

	cursor.execute("commit")
	cursor.close() # 注意及时关闭mysql连接
	src_db.close()
	print("导入完毕！")

if __name__ == '__main__':
	excel2mysql()
