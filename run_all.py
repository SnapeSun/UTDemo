# coding:utf-8
import unittest
from BeautifulReport import BeautifulReport
from common import readConfig
import os
import HTMLTestRunner
import time
import logging


curpath = os.path.dirname(__file__)
casepath = os.path.abspath(curpath)+'\\case'
print(casepath)
if not os.path.exists(casepath):
    print("测试用例需要放到'case'文件目录下")
    os.makedirs(casepath)

'''测试报告存放位置'''
reportpath = os.path.abspath(curpath)+'\\report'
if not os.path.exists(reportpath):
    os.makedirs(reportpath)


# now = time.strftime("%Y-%m-%d %H-%M-%S_") #get time
# report_filename = now+'result.html'
# report_abspath = os.path.join(reportpath,report_filename) #获得存放测试报告的位置



def all_case(case_path,rule):
    #加载测试用例
    print(casepath)
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    logging.info('{} 测试用例'.format(discover))


    return discover


def run_case(all_case,reportName="report"):
    now = time.strftime("%Y-%m-%d %H-%M-%S_")  # get time
    # report_filename = now + 'result.html'
    # report_abspath = os.path.join(reportpath, report_filename)  # 获得存放测试报告的位置

    result = BeautifulReport(all_case)
    result.report(filename=now +'report.html',description=readConfig.title,log_path=reportpath)

    # now = time.strftime("%Y-%m-%d %H-%M-%S_")
    # report_filename = now+'result.html'
    # report_abspath = os.path.abspath(reportpath)+'\\result.html'
    # report_abspath = os.path.join(reportpath,report_filename)
    # print(report_abspath)
    # file_open = open(report_abspath,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=file_open,title=u'Test Result',description=u'descriptin',verbosity=2)
    # runner.run(all_case)
    # file_open.close()

def prepare_data():
    r = "test*.py"
    discover_cases = all_case(casepath, r)
    run_case(discover_cases)


if __name__ == '__main__':

    prepare_data()
