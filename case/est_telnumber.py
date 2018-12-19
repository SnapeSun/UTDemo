# coding:utf-8
import requests
import unittest
import json, os
import sys
from common.base_config import get_data

sys.path.append('D:\\project\\UTDemo\\common\\base_config.py')


# # 引用common文件夹中的base_config.py 文件，无法引用，待存疑
# from common.base_config import msg_path
# print(msg_path)


class test_Telnumber(unittest.TestCase):

    def setUp(self):
        pass

    def test_telnum(self):

        data = get_data()
        ukey = data['ukey']
        uid = data['uid']
        print(uid)
        print(type(str(uid)))
        print(type(ukey))

        tel_url = 'http://dev.sign.xxbmm.com/customers/telephone'
        tel_header = {'channel': 'TEST', 'uid': str(uid), 'ukey': ukey, "Accept": "application/json;charset=UTF-8"}

        re = requests.get(url=tel_url, headers=tel_header)
        print(re.content.decode('utf-8'))
        data = re.content.decode('utf-8')
        dict_data = json.loads(data)
        data_msg = dict_data['msg']
        # print(data_msg)
        self.assertEqual('成功',data_msg)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()


