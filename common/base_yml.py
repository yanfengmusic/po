#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-19'
import yaml

def yml_data_with_file(file_path):
    with open("../data/"+file_path+".yml","r") as f:
        data = yaml.load(f)
        return data

