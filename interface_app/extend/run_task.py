import sys
import json
import unittest
from ddt import ddt, data, file_data, unpack
import requests
import xmlrunner

from os.path import dirname,abspath

BASE_PATH =  dirname(dirname(dirname(abspath(__file__))))
BASE_PATH.replace("\\","/")
sys.path.append(BASE_PATH)
#任务目录
TASK_PATH = BASE_PATH +"/resouce/tasks/"



@ddt
class InterfaceTest(unittest.TestCase):

    @unpack
    @file_data(TASK_PATH+"cases_data.json")
    def test_run_cases(self,url,req_methed,req_type,req_header,req_para,response_assert):

        if req_header == "{}":
            req_header ={}
        else:
            header = req_header.replace("\'", "\"")
            req_header = json.loads(header)

        if req_para == "{}":
            req_para = {}
        else:
            para = req_para.replace("\'", "\"")
            req_para = json.loads(para)


        if req_methed == "get":
            if req_type == "from":
                r = requests.get(url, headers=req_header, params=req_para)


        if req_methed == "post":
            if req_type == "from":
                r = requests.post(url, data=req_para)
            elif req_type == "json":
                r = requests.post(url, json=req_para)

# 运行测试用例
def run_cases():
    with open(TASK_PATH + 'results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)


if __name__ == '__main__':
    run_cases()