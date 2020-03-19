#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-03-07'

from appium import webdriver

def init_driver():
    # server 启动参数
    desired_caps = dict()
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8'
    desired_caps['deviceName'] = '192.168.232.246:5555'
    # app信息
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.MiuiSettings'
    # 中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
if __name__ == '__main__':

    init_driver()
