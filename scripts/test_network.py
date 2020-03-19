#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from pytest import mark

__mtime__ = '2020-03-07'

from common.base_driver import init_driver
from page.net_work_page import NetWorkPage
import pytest
from common.base_yml import yml_data_with_file


def data_with_key(key):
    return yml_data_with_file("data_search")[key]

loc_my_eqip = ("xpath", "//*[contains(@text,'我的设备')]")
loc_Personalitytheme = ("xpath", "//*[contains(@text,'个性主题')]")
loc_more = ("xpath", "//*[contains(@text,'更多设置')]")


class TestNetWork():
    loc_my_eqip = ("xpath", "//*[contains(@text,'我的设备')]")
    loc_Personalitytheme = ("xpath", "//*[contains(@text,'个性主题')]")
    loc_more = ("xpath", "//*[contains(@text,'更多设置')]")
    loc_battery = ("xpath", "//*[contains(@text,'实验')]")
    loc_search = ("xpath", "//*[contains(@text,'搜索系统设置项')]")

    def setup(self):
        self.driver = init_driver()

    @pytest.mark.parametrize("content",data_with_key("test_display")) #一个参数
    def test_display(self,content):
        nw = NetWorkPage()
        nw.scroll_buttom(self.loc_Personalitytheme, self.loc_my_eqip)
        nw.tap_more(self.loc_more)
        nw.back()
        nw.scroll_buttom(self.loc_battery, self.loc_more)
        nw.input_text(self.loc_search, content) #一个参数
        time.sleep(5)
        nw.quit_page()

    # @pytest.mark.parametrize(("username","passwd") ,[("zhangsan","123"),("lisi","345")])# 多个参数
    # def test_display(self, username,passwd):
    #     print(username,passwd)


if __name__ == '__main__':
    pass
