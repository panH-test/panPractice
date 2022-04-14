#@Author:Hanpan
#@Time:2022/4/13  18:10
#@File:secret_function.py

import hashlib
import base64

class Secret():
    '''
    md5\sha1\base64encode\base64decode加密
    '''

    def __init__(self,string):
        self._string = string.encode()

    def md5(self):
        '''
        md5加密
        :return:
        '''
        try:
            return hashlib.md5(self._string).hexdigest()
        except:
            return False

    def sha1(self):
        '''
        sha1加密
        :return:
        '''
        try:
            return hashlib.sha1(self._string).hexdigest()
        except:
            return False

    def base64encode(self):
        '''
        base64-encode
        :return:
        '''
        try:
            return base64.b64decode(self._string).decode()
        except:
            return False

    def base64decode(self):
        '''
        base64-decode
        :return:
        '''
        try:
            return base64.b64decode(self._string).decode()
        except:
            return False