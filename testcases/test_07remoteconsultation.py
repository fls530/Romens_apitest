import os
import unittest
import jsonpath
from common.handle_config import conf
from common.handle_excel import HandleExcel
from library.myddt import ddt, data
from requests import request
from common.handle_logging import log
from common.handle_path import DATA_DIR
from common.handle_data import getdata, login, EnvData

filename = os.path.join(DATA_DIR, "remote.xlsx")


@ddt
class test_01searchMemberTestCase(unittest.TestCase):
    # 01会员查询
    excel = HandleExcel(filename, "searchMember")
    cases = excel.read_data()

    @data(*cases)
    def test_searchMember(self, case):
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
        res = (
            request(
                url=url,
                method=method,
                data=data,
                headers=headers, verify=False)).json()
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
class test_02syncUserOrderCodeTestCase(unittest.TestCase):
    # 02 获取预约号
    excel = HandleExcel(filename, "syncUserOrderCode")
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        # 前置条件1:请求会员查询接口获取会员编号,设置为类属性
        url = conf.get("env", "url") + "/Inquiry"
        method = "post"
        headers = eval(conf.get("env", "headers"))
        data = {"QueryType": "searchMember", "Params": '{"SEARCH":"123456"}', "UserGuid": login()}
        res = (request(url=url, method=method, data=data, headers=headers, verify=False)).json()
        # 提取会员编号作为类属性
        EnvData.memberid = jsonpath.jsonpath(res, "$..会员编号")[0]

    @data(*cases)
    def test_syncUserOrderCode(self, case):
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
class test_03getUserVisitTemplatesTestCase(unittest.TestCase):
    # 03获取问诊输入模板
    excel = HandleExcel(filename, "getUserVisitTemplates")
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        # 前置条件1:请求搜索会员获取会员编号,设置为类属性
        url = conf.get("env", "url") + "/Inquiry"
        method = "post"
        headers = eval(conf.get("env", "headers"))
        data = {"QueryType": "searchMember", "Params": '{"SEARCH":"123456"}', "UserGuid": login()}
        res = (request(url=url, method=method, data=data, headers=headers, verify=False)).json()
        # 提取药品编号和药品名称作为类属性
        EnvData.memberid = jsonpath.jsonpath(res, "$..会员编号")[0]

        # 前置条件2:请求获取预约号设置为类属性
        url1 = conf.get("env", "url") + "/Inquiry"
        method1 = "post"
        headers1 = eval(conf.get("env", "headers"))
        data1 = {"QueryType": "syncUserOrderCode",
                 "Params": '{"ERPCODE":"","MEMBERID":"' + EnvData.memberid + '","STATE":0}', "UserGuid": login()}
        res1 = (request(url=url1, method=method1, data=data1, headers=headers1, verify=False)).json()
        # 提取药品编号和药品名称作为类属性
        EnvData.code = jsonpath.jsonpath(res1, "$..CODE")[0]

    @data(*cases)
    def test_getUserVisitTemplates(self, case):
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
        res = (
            request(
                url=url,
                method=method,
                data=data,
                headers=headers, verify=False)).json()
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
class test_04saveMemberTempTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "saveMemberTemp")
    cases = excel.read_data()

    @data(*cases)
    def test_saveMemberTemp(self, case):
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
class test_05syncEfficacyListInfoTestCase(unittest.TestCase):
    # 5 获取科室信息
    excel = HandleExcel(filename, "syncEfficacyListInfo")
    cases = excel.read_data()

    @data(*cases)
    def test_syncEfficacyListInfo(self, case):
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
class test_06syncDoctorListTestCase(unittest.TestCase):
    # 获取医生列表
    excel = HandleExcel(filename, "syncDoctorList")
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        # 前置条件1:请求搜索会员获取会员编号,设置为类属性
        url = conf.get("env", "url") + "/Inquiry"
        method = "post"
        headers = eval(conf.get("env", "headers"))
        data = {"QueryType": "searchMember", "Params": '{"SEARCH":"123456"}', "UserGuid": login()}
        res = (request(url=url, method=method, data=data, headers=headers, verify=False)).json()
        # 提取药品编号和药品名称作为类属性
        EnvData.memberid = jsonpath.jsonpath(res, "$..会员编号")[0]

        # 前置条件2:请求获取预约号设置为类属性
        url1 = conf.get("env", "url") + "/Inquiry"
        method1 = "post"
        headers1 = eval(conf.get("env", "headers"))
        data1 = {"QueryType": "syncUserOrderCode",
                 "Params": '{"ERPCODE":"","MEMBERID":"' + EnvData.memberid + '","STATE":0}', "UserGuid": login()}
        res1 = (request(url=url1, method=method1, data=data1, headers=headers1, verify=False)).json()
        # 提取药品编号和药品名称作为类属性
        EnvData.code = jsonpath.jsonpath(res1, "$..CODE")[0]

        # 前置条件3:
        # 前置条件1:请求获取科室信息获取GUID,设置为类属性
        url2 = conf.get("env", "url") + "/Inquiry"
        method2 = "post"
        headers2 = eval(conf.get("env", "headers"))
        data2 = {"QueryType": "syncEfficacyListInfo", "Params": '{"LASTTIME":0}', "UserGuid": login()}
        res2 = (request(url=url2, method=method2, data=data2, headers=headers2, verify=False)).json()
        # 提取药品编号和药品名称作为类属性
        EnvData.guid = jsonpath.jsonpath(res2, "$..GUID")[0]

    @data(*cases)
    def test_syncDoctorList(self, case):
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
class test_07addAppointmentListTestCase(unittest.TestCase):
    # 获取医生列表
    excel = HandleExcel(filename, "addAppointmentList")
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        # 前置条件1:请求搜索会员获取会员编号,设置为类属性
        url = conf.get("env", "url") + "/Inquiry"
        method = "post"
        headers = eval(conf.get("env", "headers"))
        data = {"QueryType": "searchMember", "Params": '{"SEARCH":"123456"}', "UserGuid": login()}
        res = (request(url=url, method=method, data=data, headers=headers, verify=False)).json()
        # 提取药品编号和药品名称作为类属性
        EnvData.memberid = jsonpath.jsonpath(res, "$..会员编号")[0]
        EnvData.MEMBERNAME = jsonpath.jsonpath(res, "$..会员名称")[0]
        EnvData.MEMBERPHONE = jsonpath.jsonpath(res, "$..手机号码")[0]

        # 前置条件2:请求获取预约号设置为类属性
        url1 = conf.get("env", "url") + "/Inquiry"
        method1 = "post"
        headers1 = eval(conf.get("env", "headers"))
        data1 = {"QueryType": "syncUserOrderCode",
                 "Params": '{"ERPCODE":"","MEMBERID":"' + EnvData.memberid + '","STATE":0}', "UserGuid": login()}
        res1 = (request(url=url1, method=method1, data=data1, headers=headers1, verify=False)).json()
        # 提取药品编号和药品名称作为类属性
        EnvData.code = jsonpath.jsonpath(res1, "$..CODE")[0]

        # 前置条件3:
        # 前置条件1:请求获取科室信息获取GUID,PHONE,IMID,设置为类属性
        url2 = conf.get("env", "url") + "/Inquiry"
        method2 = "post"
        headers2 = eval(conf.get("env", "headers"))
        data2 = {"QueryType": "syncEfficacyListInfo", "Params": '{"LASTTIME":0}', "UserGuid": login()}
        res2 = (request(url=url2, method=method2, data=data2, headers=headers2, verify=False)).json()
        # 提取药品编号和药品名称作为类属性
        EnvData.GUID = jsonpath.jsonpath(res2, "$..GUID")[0]

        # 前置条件4:
        # 前置条件1:请求获取医生列表GUID,PHONE,IMID,设置为类属性
        url3 = conf.get("env", "url") + "/Inquiry"
        method3 = "post"
        headers3 = eval(conf.get("env", "headers"))
        data3 = {"QueryType": "syncDoctorList",
                 "Params": '{"ORGID":"' + str(EnvData.code)[0:6] + '",'
                                                                   '"ORDER_CODE":"' + EnvData.code + '",'
                                                                                                     '"EFFID":"' + EnvData.GUID + '"',
                 "UserGuid": login()}
        res3 = (request(url=url3, method=method3, data=data3, headers=headers3, verify=False)).json()
        # 提取药品编号和药品名称作为类属性
        EnvData.DOCTORID = jsonpath.jsonpath(res3, "$..GUID")[0]
        EnvData.DOCTORPHONE = jsonpath.jsonpath(res3, "$..PHONE")[0]
        EnvData.MEMBERIMID = jsonpath.jsonpath(res3, "$..IMID")[0]

    @data(*cases)
    def test_addAppointmentList(self, case):
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
