#@Author:Hanpan
#@Time:2022/4/12  18:10
#@File:test.py

import requests
from tools import secret_function
import time

# url = 'http://120.92.35.79:8083/user/login'
# js = {
#     'phoneNumber':'13215943607',
#     'smsCode':'123456'}
#
#
# res = requests.post(url,json=js)
# print(res)
# token = res.json()['data']['token']
#
# print('token is :')
# print(token)

phoneNum = '123123'
time = str(int(time.time()*1000))
sign = phoneNum+time
md5js = secret_function.Secret(sign)

print(md5js)