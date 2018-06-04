#!/usr/bin/python
# -*- coding: utf-8 -*-
# 当keyword不是一整行的时候，而是包含于一整行中

keyword='Tl8PvPyi---A'
f = open('object.log', 'r', encoding='utf-8')
#r = open('output.log', 'w', encoding='utf-8') # 用于写入过滤到的文件内容

lines = f.readlines()
for line_1 in lines:
	if keyword in line_1:
		keyword = line_1
#print(keyword)
f.close()

f2 = open('object.log', 'r', encoding='utf-8')
line = f2.read()
log = line.split(keyword)
print(keyword + log[-1])
f2.close()
#r.close()