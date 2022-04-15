#@Author:Hanpan
#@Time:2022/4/12  18:10
#@File:login_test.py

import requests
import pytest

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
#
# phoneNum = '123123'
# time = str(int(time.time()*1000))
# sign = phoneNum+time
# md5js = secret_function.Secret(sign)
#
# print(md5js)



data_li = [
        ('13215943607','123456','1','成功'),
        ('13215943607','1','1','验证码输入不正确')
    ]

ids = ['正向用例','验证码错误']

class Test_web:

    ip = 'http://120.92.35.79:9084'
    header = {'Connect-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}

    @pytest.mark.parametrize('phoneNumber,smsCode,ctype,exp',data_li,ids=ids)
    def test_login(self,phoneNumber,smsCode,ctype,exp):
        url = self.ip+'/login'
        data = {'phoneNumber':phoneNumber,'smsCode':smsCode,'ctype':ctype}
        r = requests.post(url,json=data,headers=self.header)
        res =r.json()
        assert res['msg'] == exp



if __name__ == '__main__':
    pytest.main(['-sv','login_test.py'])