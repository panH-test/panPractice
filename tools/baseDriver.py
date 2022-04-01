import uiautomator2 as u2
from time import sleep

class DriverBase:

    def android_driver(i):
        '''

        :param i:device id or ip ,eg:32hfdsj(id)\192.168.1.1(ip)
        :return:
        '''

        d = u2.connect(i)
        return d


