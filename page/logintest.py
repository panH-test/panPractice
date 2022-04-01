#@Author:Hanpan
#@Time:2022/3/17  15:15
#@File:logintest.py

from  appium import webdriver

desired_caps={}
desired_caps["platformName"] = "Android"
desired_caps['automationName'] = 'Uiautomator1'
desired_caps['app'] = r'C:\Users\86133\.PyCharmCE2017.2\pyCode\data\pre4.1.4_03_16_16_37_release.apk'
desired_caps['udid'] = 'MYQUT20116024960'
desired_caps['deviceName'] = 'test'
desired_caps['noSign'] = True
desired_caps["unicodeKeyboard"] = True
desired_caps["resetKeyboard"] = True
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)


driver.implicitly_wait(10)
driver.find_element_by_id('com.wantong.yijian:id/tv_positive').click()
driver.find_element_by_xpath('//*[@text="允许"]').click()
driver.find_element_by_id('com.wantong.yijian:id/tab3').click()
driver.find_element_by_xpath('//*[@text="请点击登录"]').click()
driver.find_element_by_xpath('//*[@text="请输入您的手机号"]').send_keys('13215943607')
driver.find_element_by_xpath('//*[@text="请输入收到的验证码"]').send_keys('123456')
try:
    driver.find_element_by_id('com.wantong.yijian:id/iv_login_choice').click()
    driver.find_element_by_xpath('//*[@text="登录"]').click()
except :
    print('没找到用户协议同意按钮')


driver.quit()

