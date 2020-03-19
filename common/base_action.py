#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-03-12'
# from selenium import webdriver
# driber = webdriver.Chrome()
# driber.find_element()
from common.base_driver import init_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseAction():
    def __init__(self,timeout = 10,t=1):
        self.driver = init_driver()
        self.timeout = timeout
        self.t = t

    def find_ele(self,loc):
        ele = WebDriverWait(self.driver,self.timeout,self.t).until(lambda x : x.find_element(*loc))
        return ele

    def find_ele_by_EC(self,loc):
        ele = WebDriverWait(self.driver,self.timeout,self.t).until(EC.element_located_to_be_selected(loc))
        return ele

    def click(self,loc):
        ele = self.find_ele(loc)
        ele.click()

    def click_by_EC(self,loc):
        ele = self.find_ele_by_EC(loc)
        ele.click()

    def input(self,loc,text):
        ele = self.find_ele(loc)
        ele.send_keys(text)

    def input_by_EC(self,loc,text):
        ele = self.find_ele_by_EC(loc)
        ele.send_keys(text)

    def scroll(self,loc_start,loc_end):
        loc_start = self.find_ele(loc_start)
        loc_end = self.find_ele(loc_end)
        self.driver.scroll(loc_start,loc_end)

    def back_pre(self):
        self.driver.keyevent(4)

if __name__ == '__main__':

    loc_my_eqip = ("xpath", "//*[contains(@text,'我的设备')]")
    loc_Personalitytheme = ("xpath", "//*[contains(@text,'个性主题')]")
    loc_more = ("xpath", "//*[contains(@text,'更多设置')]")

    ba = BaseAction(5,6)
    ba.click(loc_my_eqip)
