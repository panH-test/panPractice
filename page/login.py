import re
from time import sleep
import os
import uiautomator2 as u2




# def get_deviceid():
#     str_init=' '
#     all_info= os.popen('adb devices').readlines()
#     # print('adb devices 输出的内容是：',all_info)
#
#     for i in range(len(all_info)):
#        str_init+=all_info[i]
#     devices_name=re.findall('\n(.+?)\t',str_init,re.S)
#
#     # print('所有设备名称：\n',devices_name)
#     return devices_name
#
#
#
# if __name__ == '__main__':
#     id = get_deviceid()
#     print(id)
#     # d = u2.connect(id)



# d =u2.connect('9ab618b7')
# d.press("home")
# d.app_start('com.wantong.yijian')
# sleep(3)
# d(resourceId="com.wantong.yijian:id/tab3").click()
# el = d(text='请点击登录')
# if el.exists(3):
#     d(text="请点击登录").click()
#
# else:
#     d.xpath(
#         '//*[@resource-id="com.wantong.yijian:id/cl_setting"]/android.view.ViewGroup[1]/android.widget.TextView[2]').click()
#     d(text="退出登录").click()



class login:

    def __init__(self):
        self.d = u2.connect('9ab618b7')
        self.d.press("home")
        self.d.app_start('com.wantong.yijian')
        sleep(3)


    def logout(self):

        # d(resourceId="com.wantong.yijian:id/tab3").click()
        # el1 = d(text='请点击登录')
        # el2 = d(test='登录')
        if self.d(text="登录").exists(3):
            login.log(self)
        elif self.d(text="请点击登录").exists(3):
            self.d(text="请点击登录").click()
        else:
            self.d.xpath(
                '//*[@resource-id="com.wantong.yijian:id/cl_setting"]/android.view.ViewGroup[1]/android.widget.TextView[2]').click()
            self.d(text="退出登录").click()
    def log(self):
        sleep(3)
        el = self.d(resourceId='com.wantong.yijian:id/et_phone')
        el.clear_text()
        el.send_keys("13211110001")
        sleep(2)
        el1 = self.d(resourceId='com.wantong.yijian:id/et_code')
        el1.clear_text()
        el1.send_keys('123456')
        sleep(2)
        self.d(text="登录").click()

    # 判断登录状态
    def logstate(self):
        pass

    # 点击登录，跳转登录页面
    def jump_login(self):
        pass
    def input_username(self):
        pass
    def input_password(self):

        pass

    def click_login_button(self):
        self.d(text="登录").click()
        sleep(2)
    def login_ok(self):
        pass


# 输入用户名
# 输入密码
# 点击登录
# 组合各步骤



if __name__ == '__main__':
    login().logout()


