# coding:utf-8
import requests,json
import os

msg_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'\\data\msg.json' #拼接msg文件的路径
print(os.path.dirname(os.path.dirname(__file__)))

u = 'http://dev.sign.xxbmm.com/customers/login'
h = {'channel':'TEST','content-type': 'application/json'}
b = {'unionid':'oPmunjiKpkBUXyn4yVXeRfqijj8w'}
# print(type(b))
jb = json.dumps(b)#将准备传入的body数据转换成str格式
# print(type(jb))
r = requests.session()
response = r.post(url=u,data=jb,headers=h,verify=False)
print(type(response))
# print(response.status_code)
# assert response.status_code
# print(type(res.content))
res = response.content.decode("utf-8")
print(res)
print(type(res))
resp = json.loads(res)
print(resp['data'])
userinfo = resp['data']



#将登陆后的uid和ukey保存在msg文件中
with open(msg_path,'w') as f:
    # if os.path.getsize(msg_path):
    #     json.dump('{}', f)
        json.dump(userinfo,f)
    # else:
    #     json.dump('{}', f)
    #     # json.dump(userinfo, f)







# json_res = json.dumps(res.content)
# print(json_res['data'])
