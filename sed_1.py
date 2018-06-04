#!/usr/bin/python
# -*- coding: utf-8 -*-
# 当keyword是一整行的时候

f = open('object.log', 'r', encoding='utf-8')
r = open('output.log', 'w', encoding='utf-8')
lines = f.read() 
keyword='---Tl8PvPyi---A--'
log = lines.split(keyword)
r.write(keyword + log[-1])
f.close()
r.close()