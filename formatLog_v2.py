#!/usr/bin/python
# -*- coding: utf-8 -*-
# 格式化squid access日志的时间戳和空格，并删除referer字段、cookie字段和UA字段
# 处理前：
# 1528779735.278     32 116.231.249.96 TCP_MEM_HIT/200 948 GET https://img.china.coach.com/css/customer.css?20180611.01  - NONE/- text/css "https://china.coach.com/" "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko" JSESSIONID=BCB78C8545046EDF102A9536102D0437-n2.C_1_2;%20route=79e613762dc1d82e7b4fc942f1eaf77d
# 处理后：
# 2018-06-12-13:02:15 32 116.231.249.96 TCP_MEM_HIT/200 948 GET https://img.china.coach.com/css/customer.css?20180611.01 - NONE/- text/css 

import re
import time
import sys

file_in = sys.argv[1]
file_out = sys.argv[2]
kongge = re.compile(r'\s+')

def format_time(timestamp):
	time_local = time.localtime(timestamp)
	time_local = time.strftime("%Y-%m-%d-%H:%M:%S", time_local)
	return time_local

f = open(file_in, 'r', encoding='utf-8')
w = open(file_out, 'w', encoding='utf-8')
lines = f.readlines()
for line in lines:
	# 转换时间戳
	unix_time = line.split()[0]
	local_time = format_time(float(unix_time))
	# 格式化多余的空格
	line = line.replace(line.split()[0], local_time)
	line = line.split('"')[0]
	line = re.sub(kongge, ' ', line)
	w.write(line + '\n')