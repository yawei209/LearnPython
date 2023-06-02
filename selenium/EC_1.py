#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author: zhangyawei

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.remote.webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# driver.maximize_window()
# driver.implicitly_wait(10)
# sleep(5)
# driver.quit()

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# driver.get('https://www.51xinwei.com')
driver.maximize_window()



############ expected_conditions 的判断方法(源地址：https://blog.csdn.net/shan286/article/details/107595626)###########
# 1、title标题
#（1）title_is      网页标题是否显示特定内容（必须完全符合），如果是返回True，否则返回False
result = EC.title_is('百度一下，你就知道')
print(result(driver))

#（2）title_contains     网页标题是否包含特定内容，如果是返回True，否则返回False
result = EC.title_contains('百度')
print(result(driver))

# 2、url网址
# （1）url_contains     网页网址是否包含特定内容，如果是返回True，否则返回False
result = EC.url_contains('baidu')
print(result(driver))

# （2）url_matches     网页网址是否匹配特定内容，如果是返回True，否则返回False
#url是https://www.baidu.com/
pattern = r'/(\w+):\/\/([^/:]+)(:\d*)?([^# ]*)/' #使用正则表达式，规定网址格式（格式要求以https开头）
result = EC.url_contains(pattern)
print(result(driver))

# （3）url_to_be      网页网址是否显示特定网址（必须完全符合），如果是返回True，否则返回False
result = EC.url_to_be('https://www.baidu.com')
print(result(driver))

# （4）url_changes     网页是否更改了，如果是返回True，否则返回False

# 3、element元素显示与可见
# （1）presence_of_element_located    特定元素是否存在于页面DOM树中，如果是，返回该元素（单个元素），否则报错
locator = (By.CLASS_NAME, 'lh')  #定位class='lh'的元素
result = EC.presence_of_element_located(locator)
print(result(driver))

# （2）presence_of_all_elements_located    定位的元素范围内，是否至少有一个元素存在于页面当中，如果是，返回满足条件的所有元素组成的List，否则返回空List？
locator = (By.CLASS_NAME, 'lh')  #定位所有class='lh'的元素
result = EC.presence_of_all_elements_located(locator)
print(result(driver))

# （3）visibility_of_element_located   特定元素是否存在于DOM树中并可见，如果是返回该元素（单个元素），否则报错
locator = (By.CLASS_NAME, 'hl')
result = EC.visibility_of_element_located(locator)

# （4）invisibility_of_element_located  特定元素是否不可访问或不存在于DOM树中，如果不存在则返回True，否则返回True
#
#        注：invisibility_of_element_located  刚好与 visibility_of_element_located的作用相反，且返回的结果大不相同。
#
# （5）invisibility_of_element 特定元素是否不可访问或不存在于DOM树中，如果不存在则返回True，否则返回True
#
#         注：invisibility_of_element_located 与 invisibility_of_element 作用类似，但前者传的是定位范围locator，后者可以是定位范围（仅text文本），也可以是元素element。
#
# （6）visibility_of  特定元素是否存在于DOM树中并可见，如果是返回该元素（单个元素），否则报错
element = driver.find_element_by_id('kw')
result = EC.visibility_of(element)
print(result(driver))

#       注：visibility_of_element_located 与  visibility_of   作用类似，但是前者传入的是定位范围locator，后者传入的是元素element，另外 invisibility_of_element  与  visibility_of   作用相反，且返回的结果大不相同。
#
# （7）visibility_of_any_elements_located   定位的元素范围内，是否至少有一个元素存在于DOM树中并可见，如果是，返回满足条件的所有元素组成的List，否则返回空List
#
# （8）visibility_of_all_elements_located  定位的元素范围内，是否所有元素都存在于DOM树中并且可见，如果是，以List形式返回元素，否则返回False
#
# （9）element_to_be_clickable  特定元素是否可点击，如果可以则返回该元素，否则返回False
locator = (By.ID, 'su') #<su>是一个可点击的按钮
result= EC.element_to_be_clickable(locator)
print(result(driver))

# 10）staleness_of    特定元素是否不再附加于于DOM树中，如果不再附加返回True，否则返回False

# 4、text文本
# （1）text_to_be_present_in_element  特定文本是否出现在特定元素中，如果是则返回True，否则返回False
locator = (By.ID, 'su')
element = EC.text_to_be_present_in_element(locator, 'submit') #查看<su>中是否包含'submit'
print(element(driver))

# （2）text_to_be_present_in_element_value  判断某文本是否是存在于特定元素的value值中，如果是则返回True，否则返回False
locator = (By.ID, 'su')
element = EC.text_to_be_present_in_element_value(locator, '百度一下') #查看<su>的value值中是否包含'百度一下'
print(element(driver)) #     注：如果该特定元素没有value值，也会返回False

# 5、frame
# （1）frame_to_be_available_and_switch_to_it   frame窗口是否可被切换，如果是返回True，否则返回False

# 6、Select
# （1）element_to_be_selected   特定元素是否被选中，如果是，返回True，否则返回False

# （2）element_located_to_be_selected

# （3）element_selection_state_to_be  特定元素的选中状态是否与预期相同，相同则返回True，不同则返回False

# （4）element_located_selection_state_to_be   特定元素的选中状态是否与预期相同，相同则返回True，不同则返回False

# 注：element_selection_state_to_be 与  element_located_selection_state_to_be  作用类似，只是传递的参数一个是元素element，一个是作用范围locator。

# 7、windows窗口
# （1）number_of_windows_to_be   特定窗口数和实际窗口数是否一致，如果是返回True，否则返回False
# windows = EC.number_of_windows_to_be(2) #期望窗口设置为2个
# print(windows(self.driver))
#
# （2）new_window_is_opened  新窗口是否打开，如果是返回True，否则返回False
# current_handles = self.driver.window_handles #获得当前所有句柄数量
# new_window = EC.new_window_is_opened(current_handles)
# print(new_window(self.driver))

# 8、alert对话框
# （1）alert_is_present     弹出框是否存在，如果是，切换到alert，否则返回false
# alert = EC.alert_is_present()
# #操作alert，例如：关闭alert
# alert.accpet()

driver.quit()
# 等待10s,等待过程中判断网页标题是否是"百度一下，你就知道"
# 如果是就继续执行后续代码，反之等待10s结束时报错(报错终止层序)
# WebDriverWait(driver,10).until(EC.title_is("百度一下，你就知道"))