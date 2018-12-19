# coding:utf-8
import requests, json, time
import urljoin
import unittest

s_url = 'http://dev.sign.xxbmm.com/customers/state'
u_query = {'unionid': 'oPmunjiKpkBUXyn4yVXeRfqijj8w'}
s_header = {'channel': 'TEST', 'uid': '163', 'ukey': '21f765af6d385c18c06f051a86036a54',
            'content-type': 'application/json', }


# json_body = json.dumps(body)

def get_url():
    for k, y in u_query.items():
        url_part = k + '=' + y
        # print(url_part)
        url = s_url + '?' + url_part
    return url


class test_Logining(unittest.TestCase):

    def setUp(self):
        pass

    def test_loginning(self):
        u = get_url()
        response = requests.get(url=u, headers=s_header, verify=False)
        # print(response.status_code)
        resp = response.content.decode('utf-8')
        res = json.loads(resp)
        data_msg = res['msg']
        self.assertEqual('成功',data_msg)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
