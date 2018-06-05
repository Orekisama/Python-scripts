#!/usr/bin/python
# -*- coding: utf-8 -*-
# 按列合并txt文件

time = open('timestamp.txt', 'r', encoding='utf-8')
host = open('host.txt', 'r', encoding='utf-8')
uri = open('uri.txt', 'r', encoding='utf-8')
signb = open('keyWordB.txt', 'r', encoding='utf-8')
signf = open('keyWordF.txt', 'r', encoding='utf-8')
signh = open('keyWordH.txt', 'r', encoding='utf-8')

timeLine = time.readlines()
hostLine = host.readlines()
uriLine = uri.readlines()
signbLine = signb.readlines()
signfLine = signf.readlines()
signhLine = signh.readlines()

newfile = open('test.txt', 'w')
if len(timeLine) == len(hostLine) == len(uriLine):
	for num in range(0, len(timeLine)):
		line = timeLine[num].strip('\n') + "**" + hostLine[num].strip('\n') + "**" + uriLine[num].strip('\n') + "**" + signbLine[num].strip('\n') + "**" + signfLine[num].strip('\n') + "**" + signhLine[num].strip('\n') + '\n'
		print(line)
		newfile.write(line)

time.close()
host.close()
uri.close()
signb.close()
signf.close()
signh.close()

