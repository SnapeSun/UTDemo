# coding:utf-8
import json,os
from common.processing_json import get_json
from wxpy import *

# bot = Bot()
# f =bot.friends().search('李')
# print(f)

# s_url = 'http://dev.sign.xxbmm.com/customers/state'
# s_header = {'channel':'TEST','uid':'163','ukey':'21f765af6d385c18c06f051a86036a54','content-type': 'application/json',}
# body = {'unionid':'oPmunjiKpkBUXyn4yVXeRfqijj8w'}
# json_body = json.dumps(body)

# for k,y in body.items():
#     url_part = k+'='+y
#     print(url_part)
# url = s_url+'?'+url_part
# print(url)


# 引用common文件夹中的base_config.py 文件，无法引用，待存疑
# from common.base_config import msg_path
# print(msg_path)


# curpath = os.path.dirname(os.path.dirname(__file__))
# print(curpath)
# casepath = os.path.abspath(curpath)+'\\case'
# print(casepath)




from ddt import data,unpack,ddt,file_data
import unittest
import time
now = time.strftime("%Y-%m-%d")
print(now)

request_parameter_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'\\data\Request_parameter.json'
login_msg_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'\\data\msg.json'
Headers = get_json(request_parameter_path)
login_msg = get_json(login_msg_path)
for k, v in Headers.items():
    if k in ['uid', 'ukey']:#根据键值对中的键，去查找到uid与ukey对应的键值对
        if login_msg != {}:#判断登录后存储的信息不为空
            if isinstance(login_msg[k],int):#如果字典中，K对应的value值为int类型，则转换为string类型
                Headers[k] = str(login_msg[k])
                # print('------')
                # print(Headers[k])
            Headers[k] = login_msg[k]   #将登录后存入的信息根据键值 拿到value值，在赋予 Headers中 键值相对应的Value值


# @ddt
# class Test_DDT(unittest.TestCase):
#     def setUp(self):
#         print('This is setup')
#
#
#     def tearDown(self):
#         print('This is teardown')
#
#     @data([3,2,1],[7,6,5])
#     def  test_1(self,data):
#         print(data)
#
#     @data([1,2,3],[5,6,11])
#     @unpack
#     def test_2(self,a,b,sum):
#         s = int(a)+int(b)
#         self.assertEqual(s,int(sum))
#
#     @file_data('msg.json')
#     def test_3(self,value):
#         print(value)
#
#
#
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

