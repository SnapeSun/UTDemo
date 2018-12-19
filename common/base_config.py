# coding:utf-8
import os
import json
import logging
from common.Write_Excel import excel_write_result
import codecs

msg_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\data\msg.json'  # 拼接msg文件的路径


def get_data():
    with open(msg_path, 'r') as f:
        # try:
        # print('====' * 2)
        line = f.readline()
        d = json.loads(line)
        print(type(d))
    return d


def write_data(data, data_path):  # 把登录数据写入msg.json文件
    if isinstance(data, dict):
        with open(data_path, 'w', encoding='utf-8') as f:
            json.dump(data, f)
            logging.info('interface params total:{} , write to msg.json successfully!\n'.format(len(data)))
    else:
        logging.info('{} params is not dict! \n'.format(write_data.__name__))


def write_result(result,filename = ''):
    # filename = r'D:\project\UTDemo\report\test_result.xlsx'
    row_num = result['rowNum']  # 获取返回结果的行数
    print('>>>>>>>>>>>>>>>>>>>>row_num')
    # 结果写入Excel表格
    write_excel = excel_write_result(filename)
    write_excel.write(row_num, 9, result['status_code'])  # 写入返回状态码status_code,第9列
    write_excel.write(row_num, 12, result['error'])  # 状态码非200时或系统状态码异常时的返回信息
    write_excel.write(row_num, 14, result['result'])  # 结果
    write_excel.write(row_num, 15, result['msg'])  # 抛异常
