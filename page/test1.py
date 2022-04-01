#@Author:Hanpan
#@Time:2021/12/24  14:28
#@File:test1.py


import uiautomator2 as u2
import time


d=u2.connect('192.168.26.101')

d.healthcheck()

d.debug = False
# d.info("com.wantong.yijian")

d.app_stop_all()
# d.app_install('..\data\intest4.0.6_12_22_15_29_release.apk')
d.app_start('com.wantong.yijian','.business.view.activity.MainActivity')

# print(d.current_app())
# print(d.serial)
# print(d.wlan_ip)
# print(d.device_info)




# 登录
d(resourceId="com.wantong.yijian:id/tab3").click()
time.sleep(0.3)
if d(resourceId="com.wantong.yijian:id/textView3").exists:
    print('已登录')

else:
    d(resourceId="com.wantong.yijian:id/tv_login").click(timeout=3)
    d(resourceId="com.wantong.yijian:id/et_phone").set_text('19900000001')

    d(resourceId="com.wantong.yijian:id/et_code").send_keys('123456')
    time.sleep(1)
    d(scrollable=True).fling.toEnd()
    time.sleep(1)

    d(resourceId="com.wantong.yijian:id/iv_login_choice").click()
    time.sleep(1)
    d(resourceId="com.wantong.yijian:id/tv_login").click()

    if d(resourceId="com.wantong.yijian:id/textView3").exists:
        print('登录成功')