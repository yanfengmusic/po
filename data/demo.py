#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-18'

import yaml

# 读出来
with open("./data_test.yml","r") as f:
    data = yaml.load(f,Loader=yaml.FullLoader)#如果不加Loader=yaml.FullLoader每次执行都会提示不安全的警告
    print(data)

# 写进去
# data = {'Search_Data': {
#         'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
#         'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}
#
# with open("./text.yaml", "w") as f:  # 在当前目录下生成text.yaml文件，若文件存在直接更新内容
#     yaml.dump(data, f, encoding='utf-8', allow_unicode=True)
