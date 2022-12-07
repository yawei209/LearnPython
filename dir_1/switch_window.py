#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#Author: zhangyawei

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
driver.maximize_window()

print("页面的title： ",driver.title)


# 获得百度搜索窗口句柄
search_windows = driver.current_window_handle
print("百度搜索窗口句柄: ",search_windows)

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text("立即注册").click() #点击注册会打开新窗口并保持到新窗口

# 获得当前所有打开的窗口的句柄
all_handles = driver.window_handles
print("所有打开的窗口的句柄: ",all_handles)

# 切换到注册窗口 方式1 通过判断是否与当前窗口句柄一致
# for handle in all_handles:
#     if handle != search_windows:
#         driver.switch_to.window(handle)
#         driver.find_element_by_name("userName").send_keys('我是测试小白')
#         driver.find_element_by_name('phone').send_keys('12345678910')
#         time.sleep(2)
#         # 后续步骤省略

# 切换到注册窗口 方式2 通过获取的所有窗口列表的索引切换
# driver.switch_to.window(all_handles[1])
# driver.find_element_by_name("userName").send_keys('我是测试小白')
# driver.find_element_by_name('phone').send_keys('12345678910')
# time.sleep(2)

driver.switch_to.window(all_handles[0])
time.sleep(1)
driver.switch_to.window(all_handles[-1])
time.sleep(1)
driver.close() #关闭当前所在窗口
# driver.quit()