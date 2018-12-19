import unittest
import ddt
import os
import requests
from common.readExcel import ExcelUtil
from common.Write_Excel import excel_write_result, copy_excel
from common import Requests_api
from common.base_config import write_result, write_data
from common.Requests_api import login_msg_path
import time
import codecs
from common.logger import Log
import BeautifulReport

now = time.strftime("%Y-%m-%d_%H-%M-%S_")
# report_copy_excel_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) +'\\report\copy_interface_case.xlsx'
# report_copy_excel = os.path.join(os.path.abspath(os.path.dirname(__file__)) + '\\report',
#                                  now + 'copy_interface_case.xlsx')  # 存放复制测试用例接口数据的Excel
result_xlsx = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + '\\report'),
                           now + 'result.xlsx')  # 该表格接收请求数据的返回结果


print(result_xlsx)
data_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\data\Interface_case.xlsx'  # 各个接口case存放的位置
# print(data_path)
data_name = '\\' + now + 'copy_interface_case.xlsx'
report_copy_excel = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\data' + data_name
# print(report_copy_excel)
# print(report_copy_excel)

test_data = ExcelUtil(data_path).data_dict()
            # print(test_data)

@ddt.ddt
class myTest_T(unittest.TestCase):

    # setup、teardown方法在每执行一个TestCase时，都会重新执行一遍，
    # 当只想要在整个文件中进行一次setup和teardown操作的时候，
    # 可以用setUpClass、tearDownClass
    @classmethod
    def setUpClass(cls):
        cls.log = Log()
        print('>>>>>>>>>>>>>>>>>>>setupClass')
        cls.s = requests.session()  # 获取requests session
        copy_excel(data_path, result_xlsx)  # 复制测试用例接口数据到新的Excel

    @ddt.data(*test_data)
    def test_T(self, data):
        print(data)
        print('>>>>>>>>>>>>>>>>send_requests')
        res = Requests_api.send_requests(self.s, data)
        print(res)
        if res:
            write_result(res,filename = result_xlsx)
            check = data['checkpoint']
            self.log.info('原设定的检查点---> %s' % check)
            result_check = res['text']
            self.log.info('请求结果返回的检查点---> %s' % result_check)
            self.assertTrue(check in result_check, 'the check result is false')
            self.log.info('{} {} interface execute success '.format(data['id'], data['name']))

    @classmethod
    def tearDownClass(cls):
        write_data({}, login_msg_path)  # clear msg.json data
        # cls.log.info('Test environment')


if __name__ == '__main__':
    # discover = unittest.defaultTestLoader.discover(os.path.abspath(os.path.dirname(__file__))+'\\case', pattern='text*.py', top_level_dir=None)
    # result = BeautifulReport(discover)
    unittest.main(verbosity=2)

    '''
    UTDemo Catalog
    run_all：this is total entrance
    Test_T：execute test case ,ddt
    Requests_api.py send requests ,return response
    
    
    '''
