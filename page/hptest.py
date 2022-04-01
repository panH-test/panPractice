

import re
import logger
import os
import uiautomator2 as u2

# def init_driver(self,device_name):
#     '''
#
#     :param self:
#     :param devices_name:
#     :return:
#     '''
#
#     try:
#         u2.logger.info(device_name)
#         d = u2.connect(device_name)
#         d.wait_timeout = 20
#         d.click_post_delay=5
#         u2.logger('连接设备：{}'.format(device_name))
#         return d
#     except Exception as e:
#         u2.logger.info('初始化driver异常！{}'.format(e))
#
#     d.app_start('com.wantong.yijian')
# # def findDevices():
# rst = os.system('adb devices')
# devices = re.findall(r'(.*?)\s+device',rst)
# if len(devices) > 1:
#     deviceIds = devices[1:]
#     logger.info('共找到%s个手机'%str(len(devices)-1))
#     for i in deviceIds:
#         u2.logger.info('IDwei %s'%i)
#         # return deviceIds
# else:
#     u2.logger.error('no such')
#         # return
#
# # if __name__ == '__main__':
# #     findDevices()


