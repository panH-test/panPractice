#@Author:Hanpan
#@Time:2022/3/18  12:31
#@File:HuaweiSetting.py

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


desired_caps={}
desired_caps['platformName'] = 'android'
desired_caps['platformVersion'] = '10.0'
desired_caps['automationName'] = 'uiautomator1'
desired_caps['deviceName'] = 'huawei'
desired_caps['udid'] = 'MYQUT20116024960'
desired_caps['appPackage']='com.android.settings'
desired_caps['appActivity'] = '.HWSettings'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@text="WLAN"]').click()
el = driver.find_element_by_xpath('//*[@text="YDSWZX_3F"]')
TouchAction(driver).long_press(el).perform()
driver.find_element_by_xpath('//android.widget.LinearLayout[2]').click()
driver.find_element_by_xpath('//*[@text="代理"]').click()
driver.find_element_by_xpath('//*[@text="手动"]').click()
driver.find_element_by_xpath('//*[@text="proxy.example.com"]').send_keys('192.168.26.211')
driver.find_element_by_xpath('//*[@text="8080"]').send_keys('8888')
driver.find_element_by_xpath('//*[@text="保存"]').click()
driver.quit()