import json
import requests
#http://dev.sign.xxbmm.com/customers/login
# body = {'unionid':'oPmunjiKpkBUXyn4yVXeRfqijj8w'}
# u ="http://dev.sign.xxbmm.com/customers/login"
# h = {'channel':'BEAUTY'}
# json_body = json.dumps(body)
# s =requests.sessions()


def login(sess,cha,unid):

    u = "http://dev.sign.xxbmm.com/customers/login"

    h = {"channel":cha,'content-type':'application/json'}

    b = {"unionid":unid}
    json_b = json.dumps(b)

    r = sess.post(url=u,headers=h,data=json_b,verify=False)
    print(r.status_code)
    return r.content.decode("utf-8") #python3


def is_login_sucess(res):
    if "10008" in res:
        return False
    elif "10001" in res:
        return True
    else:
        return False

if __name__ == '__main__':
    s = requests.session()
    co = s.cookies
    print(co)
    re = login(s,"TEST","oPmunjiKpkBUXyn4yVXeRfqijj8w")
    json_re =json.loads(re)
    print(json_re['data'])
    result = is_login_sucess(re)
    print(result)

