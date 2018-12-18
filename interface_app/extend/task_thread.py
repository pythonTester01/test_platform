import json
import os
import threading
from time import sleep
from interface_app.models import TestTask,TestCase,TestResult
from interface_app.apps import TASK_PATH,RUN_TASK_FILE
from xml.dom import minidom

class TaskThread():
    ''''实现测试任务的多线程'''

    def __init__(self,tid):
        self.tid = tid

    def run_tasks(self,tid):
        task_obj = TestTask.objects.get(id=tid)

        case_list = task_obj.cases.split(",")
        case_list.pop(-1)

        #修改状态为执行中。。。
        task_obj.status=1
        task_obj.save()

        # 运行函数
        # run_cases()
        cases_all = {}
        for case_id in case_list:
            print(case_id)
            cases_obj = TestCase.objects.get(pk=case_id)

            case_dict = {
                "url": cases_obj.url,
                "req_methed": cases_obj.req_methed,
                "req_type": cases_obj.req_type,
                "req_header": cases_obj.req_header,
                "req_para": cases_obj.req_para,
                "response_assert": cases_obj.response_assert
            }
            cases_all[cases_obj.id] = case_dict
        json_str = json.dumps(cases_all)
        case_data_file = TASK_PATH + "cases_data.json"
        with open(case_data_file, "w+") as f:
            f.write(json_str)

        # 运行测试json文件
        os.system("python3 " + RUN_TASK_FILE)


    def run(self):
        threads = []
        t = threading.Thread(target=self.run_tasks,args=(self.tid,))
        threads.append(t)

        for i in threads:
            i.start()

        for i in threads:
            i.join()

        sleep(2)

        self.save_result()

        task_obj = TestTask.objects.get(id=self.tid)
        #执行完成
        task_obj.status = 2
        task_obj.save()



    def run_new(self):
        threads = []
        t = threading.Thread(target=self.run)
        threads.append(t)

        for i in threads:
            i.start()


    def save_result(self):
        dom = minidom.parse(TASK_PATH +"results.xml")
        root = dom.documentElement
        ts = root.getElementsByTagName("testsuite")
        name = ts[0].getAttribute("name")
        errors = ts[0].getAttribute("errors")
        failures = ts[0].getAttribute("failures")
        skipped = ts[0].getAttribute("skipped")
        tests = ts[0].getAttribute("tests")
        run_time = ts[0].getAttribute("time")
        # print("errors", ts[0].getAttribute("errors"))
        # print("failures", ts[0].getAttribute("failures"))
        # print("tests", ts[0].getAttribute("tests"))

        with open((TASK_PATH +"results.xml"),"r",encoding="utf-8") as file:
            result = file.read()


        # TestResult.objects.create("") 保存到结果表里面
        TestResult.objects.create(name=name,errors=errors,
                                  failures=failures,skipped=skipped,
                                  tests=tests,run_time=run_time,
                                  task_id = self.tid,result=result)