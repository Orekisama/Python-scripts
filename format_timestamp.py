#!/usr/bin/python
# -*- coding: utf-8 -*-
# format timestamp from unix time to real time of squid access log 

import sys
import time

def real_time(timestamp):
	time_local = time.localtime(timestamp)
	time_format = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
	return time_format

file_in = open('inputlog.txt', 'r', encoding='utf-8')
file_out = open('outputlog.txt', 'w', encoding='utf-8')
lines = file_in.readlines()
for line in lines:
	unix_time = line.split()[0]
	log_real_time = real_time(float(unix_time))
	new_line = line.replace(line.split()[0], log_real_time)
	file_out.write(new_line)