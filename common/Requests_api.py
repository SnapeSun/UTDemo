import requests
import json
import os
import logging
from common.processing_json import get_json
from common.base_config import get_data, write_data
from common import readConfig
from common.readExcel import ExcelUtil
from common import logger
import requests

# from case.Test_T import test_data

request_parameter_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\data\Request_parameter.json'
login_msg_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\data\msg.json'
body_data_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\data\\bodyData.json'
print(body_data_path)


'''封装requests请求'''


def send_requests(s, data):
    print('send_requests>>>>>>>>>>>>>>>>>>>>')
    print(data)
    if not isinstance(data, dict):
        raise TypeError('{}该参数不是字典类型'.format(send_requests(__name__)))

    if data['skip'] == 'true':  # 逐条判断测试case是否执行
        logging.info('{}{}接口 测试用例不执行'.format(data[id], data['name']))
        return False

    else:
        request_method = data['method']  # 获取请求方式
        url = data['url']
        type = data['type']
        testcase_id = data['id']
        testcase_name = data['name']
        try:
            params = eval(data['params'])  # 判断测试case中params是否有值，有的话，则转成字典类型
        except:
            params = None  # 如果params 为空，则赋值为none
        Headers = get_json(request_parameter_path)
        login_msg = get_json(login_msg_path)  # 取出登录时获取到的信息

        # 判断表格中的headers,若是 Yes，则需要headers数据
        if data['headers'] == 'yes':
            for k, v in Headers.items():
                if k in ['uid', 'ukey']:  # 根据键值对中的键，去查找到uid与ukey对应的键值对
                    if login_msg != {}:  # 判断登录后存储的信息不为空
                        # if type(login_msg[k]) == 'int':
                        #     Headers[k] = repr(login_msg[k])
                        if isinstance(login_msg[k], int):  # 如果字典中，K对应的value值为int类型，则转换为string类型
                            Headers[k] = repr(login_msg[k])
                            # print('------')
                            logging.info('id 值为--------------->'+Headers[k])

                        else:
                            Headers[k] = login_msg[k]  # 将登录后存入的信息根据键值 拿到value值，在赋予 Headers中 键值相对应的Value值
        else:
            Headers = None

        # 判断body值
        try:
            body_data = eval(data['body'])  # 若body一列存在值，则转换成字典类型
        except:
            body_data = {}  # 若报错则说明没有值，则赋值空

        if data['type'] == 'data':
            body = body_data

        elif data['type'] == 'json':
            body = get_json(body_data_path, data['body']) #body拿到一组unionID的键值对 "unionid": ""
            for k, v in body.items():
                if k == 'unionid':
                    if data['unionid'] == 'true':#判断从表格中取到的每条case中的unionID值是否填写的为true
                        pass
                    else:
                        body[k] = readConfig.new_unionid
        else:
            body = body_data
        if data['headers'] == 'yes':  # headers 为 yes 时， body数据需要转为字符串类型
            body = json.dumps(body)

        if request_method == 'get':  # 除post请求外，其他请求方式默认传参数params
            params = body
            if data['params'] == 'true':
                pass
            else:
                params = json.loads(params)
            body = None

        logging.info('**** Execute Test Case {} {} ***'.format(testcase_id, testcase_name))
        logging.info('*** request method and url is {} {} ***'.format(request_method, url))
        logging.info('*** request header and body is {} {} ***'.format(Headers, body))


        try:
            response = s.request(method=request_method, url=url, headers=Headers, data=body, verify=False)

            res = {}  # 接收返回数据

            logging.info('---information for return：%s' % response.content.decode("utf-8"))
            res['id'] = data['id']
            res['name'] = data['name']
            res['rowNum'] = data['rowNum']
            res['status_code'] = str(response.status_code)  # 状态码转成str
            res['text'] = response.content.decode('utf-8')
            res['time'] = response.elapsed.total_seconds()  # 接口请求时间转str

            if res['status_code'] != '200':  # 判断返回code是否正常
                res['error'] = res['text']
            else:
                res['error'] = ''
            if data['checkpoint'] in res['text']:  # 断言,判断返回信息是否正确
                res['result'] = 'pass'
                logging.info('******* the result of test case is %s ------>%s' % (testcase_id, res['result']))

                if testcase_id == 'test_04':  # 如果是正常登录case，则把返回的有用参数保存到msg.json
                    login_msg = json.loads(res['text'])['data']
                    write_data(login_msg, login_msg_path)  # 登录参数写入json文件
            else:
                res['result'] = 'fail'  # 断言失败结果
            res['msg'] = ''
            return res
        except Exception as error_msg:
            logging.error('请求异常!{}'.format(error_msg))
            res['msg'] = str(error_msg)  # 出现异常，保存错误信息
            res['result'] = 'error'  # 结果保存错误
            return res


if __name__ == '__main__':
    excel_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\data\Interface_case.xlsx'
    print(excel_path)
    data = ExcelUtil(excel_path, 'Sheet1')
    print(type(data))

    print(data.data_dict(make=False))

    # s = requests.session()
    # res = send_requests(s,data[2])
