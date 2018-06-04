#!/usr/bin/python
# -*- coding: utf-8 -*-

f = open('object.log', 'r', encoding='utf-8')
r = open('output.log', 'w', encoding='utf-8')
lines = f.read() 
keyword='---Tl8PvPyi---A--'
log = lines.split(keyword)
print(log[-1])