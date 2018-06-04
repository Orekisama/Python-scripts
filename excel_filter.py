#!/usr/bin/python
# -*- coding: utf-8 -*-
# 按照指定要求过滤excel文件，并将结果输出到新的excel中

import pandas as pd
from pandas import *
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

sheetName = 'SalesForce'
data_frame = pd.read_excel(input_file, sheetName, index_col=None)
# 每个data_frame即为一个列标题，'=='后代表此列需要过滤的条件，可以有多个条件
data_frame_value_meets_condition = data_frame[(data_frame[u'dig查询结果'] == u'yes') & (data_frame[u'地区'] == u'大陆')]
writer = pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(writer, sheet_name = 'illegal_records_output', index = False)
writer.save()
