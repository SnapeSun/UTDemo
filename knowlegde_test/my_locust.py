# coding : utf-8
from locust import HttpLocust,TaskSet,task
import json
import os

# u = 'http://dev.sign.xxbmm.com/customers/login'
h = {'channel':'TEST','content-type': 'application/json'}
b = {'unionid':'oPmunjiKpkBUXyn4yVXeRfqijj8w'}
msg_data_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'\\data\msg.json'
# class user_todo(TaskSet):
#
#     @task
#     def xxbmm_sign(self):
#         self.client.get("/")
#
#
# class user(HttpLocust):
#
#     task_set = user_todo
#     min_wait = 3000
#     max_wait = 6000
#     host = "https://www.baidu.com"

def write_msg(data,path):
    with open(path,'w') as f:
        json.dump(data,f)

def read_msg(path):
    with open(path,'r')as f:
        line = f.readline()
        data = json.loads(line)
    return data

def get_new_url(old_url,union_data):
    for k,v in union_data.items():
        part = k + '=' + v
        new_url = old_url + '?' + part
    return new_url


class interface_xxbmm(TaskSet):

    def on_start(self):
        u = 'http://dev.sign.xxbmm.com/customers/login'
        jb = json.dumps(b)
        response =self.client.post(url=u,data= jb,headers = h,verify = False)
        res = json.loads(response.content.decode("utf-8"))
        msg_data = res['data']
        write_msg(msg_data,msg_data_path)

    @task(3)
    def check_telephone(self):
        url = '/customers/telephone'
        data = read_msg(msg_data_path)
        uid = data['uid']
        ukey = data['ukey']
        tel_header = {'channel': 'TEST', 'uid': str(uid), 'ukey': ukey, "Accept": "application/json;charset=UTF-8"}
        self.client.get(url= url,headers= tel_header)

    @task(2)
    def get_account(self):
        url = '/customers/account'
        data = read_msg(msg_data_path)
        uid = data['uid']
        ukey = data['ukey']
        tel_header = {'channel': 'TEST', 'uid': str(uid), 'ukey': ukey, "Accept": "application/json;charset=UTF-8"}
        self.client.get(url=url, headers=tel_header)

    @task(1)
    def get_logining(self):
        url = '/customers/state'
        new_url =get_new_url(url,b)
        data = read_msg(msg_data_path)
        uid = data['uid']
        ukey = data['ukey']
        tel_header = {'channel': 'TEST', 'uid': str(uid), 'ukey': ukey, "Accept": "application/json;charset=UTF-8"}
        self.client.get(url=url, headers=tel_header)



class my_user(HttpLocust):
    task_set = interface_xxbmm
    min_wait = 1000
    max_wait = 3000
    host = 'http://dev.sign.xxbmm.com'




