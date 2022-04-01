import uiautomator2 as u2
import time

# 连接设备
d = u2.connect('192.168.26.101')
# 启动app
d.app_start("com.wantong.yijian")
time.sleep(5)
# 切换底部tab
# d.xpath('//*[@resource-id="com.wantong.yijian:id/tab3"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
# d.xpath('//*[@resource-id="com.wantong.yijian:id/tab1"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
# d.xpath('//*[@resource-id="com.wantong.yijian:id/tab1"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
# d.xpath('//*[@resource-id="com.wantong.yijian:id/tab0"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
# d.click(0.592, 0.96)
# try:
#     # d(resourceId="com.wantong.yijian:id/tab_main").click()
#     # d.xpath('//*[@resource-id="com.wantong.yijian:id/tab3"]').click()
#     d(resourceId="com.wantong.yijian:id/tab3").click()
#     time.sleep(3)
#     d(resourceId="com.wantong.yijian:id/tv_end", text="去认证").click()
# except Exception as e:
#     print("no such element,error:",e)


# app stop
# d.app_stop("com.wantong.yijian")
# click home button
d(resourceId='com.wantong.yijian:id/tab0').click()
d(resourceId='com.wantong.yijian:id/tab_main').click()
d.swipe_points([(0,320),(0,1100)],0.1)

d(resourceId='com.wantong.yijian:id/tab1').click()
d(resourceId='com.wantong.yijian:id/tab3').click()