#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

# 计算总流量
band = []
band_group = []

csv_file = csv.reader(open('acs.csv', 'r'))
#print(csv_file)
for line in csv_file:
	band.append(float(line[1]))
#print(sum(band)/1024/1024/1024, 'G')
print("total bandwidth is:", '{:.2f}'.format(sum(band)/1024/1024/1024) + 'G')

# 计算指定设备组的流量
f = open(r'servers_100.txt', 'r')
servers = f.readlines()
for server in servers:
	csv_file = csv.reader(open('acs.csv', 'r'))
	for line in csv_file:
		if server.strip('\n') == line[0]:
			#print(line[1])
			band_group.append(float(line[1]))
print("servers bandwidth is:", '{:.2f}'.format(sum(band_group)/1024/1024/1024) + 'G')