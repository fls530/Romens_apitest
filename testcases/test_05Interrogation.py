import os
import unittest
import jsonpath
from common.handle_excel import HandleExcel
from library.myddt import ddt, data
from requests import request
from common.handle_config import conf
from common.handle_logging import log
from common.handle_path import DATA_DIR
from common.handle_data import getdata, login, EnvData

filename = os.path.join(DATA_DIR, "Interrogation.xlsx")


@ddt
class test_01getDiseaseListTestCase(unittest.TestCase):
    # 获取病症列表
    excel = HandleExcel(filename, "getDiseaseList")
    cases = excel.read_data()

    @data(*cases)
    def test_getDiseaseList(self, case):
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
        res = (
            request(url=url, method=method, data=data, headers=headers, verify=False)).json()
        try:
            self.assertEqual(expected, res["result"])
        except AssertionError as e:
            # 结果回写excel中
            log.error("用例--{}--执行未通过".format(case["title"]))
            log.debug("预期结果：{}".format(expected))
            log.debug("实际结果：{}".format(res))
            log.exception(e)
            self.excel.write_data(row=row, column=8, value="未通过")
            raise e
        else:
            # 结果回写excel中
            log.info("用例--{}--执行通过".format(case["title"]))
            self.excel.write_data(row=row, column=8, value="通过")


@ddt
class test_02getDrugListTestCase(unittest.TestCase):
    # 搜索药品
    excel = HandleExcel(filename, "getDrugList")
    cases = excel.read_data()

    @data(*cases)
    def test_getDiseaseList(self, case):
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
        res = (
            request(url=url, method=method, data=data, headers=headers, verify=False)).json()
        try:
            self.assertEqual(expected, res["result"])
        except AssertionError as e:
            # 结果回写excel中
            log.error("用例--{}--执行未通过".format(case["title"]))
            log.debug("预期结果：{}".format(expected))
            log.debug("实际结果：{}".format(res))
            log.exception(e)
            self.excel.write_data(row=row, column=8, value="未通过")
            raise e
        else:
            # 结果回写excel中
            log.info("用例--{}--执行通过".format(case["title"]))
            self.excel.write_data(row=row, column=8, value="通过")


@ddt
class test_03syncDoctorListTestCase(unittest.TestCase):
    # 获取医生列表
    excel = HandleExcel(filename, "syncDoctorList")
    cases = excel.read_data()

    @data(*cases)
    def test_getDiseaseList(self, case):
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
        res = (request(url=url, method=method, data=data, headers=headers, verify=False)).json()
        try:
            self.assertEqual(expected, res["result"])
        except AssertionError as e:
            # 结果回写excel中
            log.error("用例--{}--执行未通过".format(case["title"]))
            log.debug("预期结果：{}".format(expected))
            log.debug("实际结果：{}".format(res))
            log.exception(e)
            self.excel.write_data(row=row, column=8, value="未通过")
            raise e
        else:
            # 结果回写excel中
            log.info("用例--{}--执行通过".format(case["title"]))
            self.excel.write_data(row=row, column=8, value="通过")


@ddt
class test_04saveOrderByAfterTestCase(unittest.TestCase):
    # 提交预约问诊
    excel = HandleExcel(filename, "saveOrderByAfter")
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        # 前置条件1:请求搜索药品接口获取药品返回信息,设置为类属性
        url1 = conf.get("env", "url") + "/Inquiry"
        method1 = "post"
        headers1 = eval(conf.get("env", "headers"))
        data1 = {"QueryType": "getDrugList",
                 "Params": '{"page":1,"keyword":"' + conf.get("test_data", "drugs") + '","barcode":""}',
                 "UserGuid": login()}
        res1 = (request(url=url1, method=method1, data=data1, headers=headers1, verify=False)).json()
        # 提取药品编号和药品名称作为类属性
        EnvData.drugs_id = jsonpath.jsonpath(res1, "$..GUID")[0]
        EnvData.goodsname = jsonpath.jsonpath(res1, "$..GOODSNAME")[0]

        # 前置条件2: 请求获取医生列表,获取医生ID和医生手机号,设置为类属性
        url2 = conf.get("env", "url") + "/Inquiry"
        method2 = "post"
        headers2 = eval(conf.get("env", "headers"))
        data2 = {"QueryType": "syncDoctorList", "Params": '{"keyword":""}', "UserGuid": login()}
        res2 = (request(url=url2, method=method2, data=data2, headers=headers2, verify=False)).json()
        # 提取医生接口返回值 医生编号,医生手机号
        try:
            EnvData.doctorId = jsonpath.jsonpath(res2, "$..GUID")[0]
            EnvData.doctorPhone = jsonpath.jsonpath(res2, "$..PHONE")[0]
        except Exception as e:
            print("没有医生在线")

    @data(*cases)
    def test_getDiseaseList(self, case):
        # 请求提交预约问诊接口
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
        res = (request(url=url, method=method, data=data, headers=headers, verify=False)).json()
        try:
            self.assertEqual(expected, res["result"])
        except AssertionError as e:
            # 结果回写excel中
            log.error("用例--{}--执行未通过".format(case["title"]))
            log.debug("预期结果：{}".format(expected))
            log.debug("实际结果：{}".format(res))
            log.exception(e)
            self.excel.write_data(row=row, column=8, value="未通过")
            raise e
        else:
            # 结果回写excel中
            log.info("用例--{}--执行通过".format(case["title"]))
            self.excel.write_data(row=row, column=8, value="通过")
