#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-03-12'

from common.base_action import BaseAction

loc_my_eqip =("xpath","//*[contains(@text,'我的设备')]")
loc_Personalitytheme = ("xpath","//*[contains(@text,'个性主题')]")
loc_more = ("xpath","//*[contains(@text,'更多设置')]")
loc_battery = ("xpath","//*[contains(@text,'实验')]")
loc_search = ("xpath","//*[contains(@text,'搜索系统设置项')]")

class NetWorkPage(BaseAction):
    def scroll_buttom(self,loc_Personalitytheme,loc_my_eqip):
        """
        从个性主题滑动到我的设备
        :param locator_start:
        :param locator_end:
        :return:
        """
        self.scroll(loc_Personalitytheme,loc_my_eqip)

    def tap_more(self,loc_more):
        """点击更多"""
        self.click(loc_more)

    def back(self):
        """返回"""
        self.back_pre()

    def input_text(self,loc,text):
        "搜索项输入信息"
        self.input(loc,text)

    def quit_page(self):
        "退出"
        self.driver.quit()
        
        
     def quit_page111(self):
        "退出"
         pass


if __name__ == '__main__':
    nw = NetWork()
    nw.scroll_buttom(loc_Personalitytheme,loc_my_eqip)
    nw.tap_more(loc_more)
    nw.back()
    nw.scroll_buttom(loc_battery,loc_more)
    nw.input_text(loc_search,"设置")
    nw.quit_page()
