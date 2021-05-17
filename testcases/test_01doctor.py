import os
import unittest
from common.handle_excel import HandleExcel
from library.myddt import ddt, data
from requests import request
from common.handle_logging import log
from common.handle_path import DATA_DIR
from common.handle_data import getdata

filename = os.path.join(DATA_DIR, "doctor.xlsx")


@ddt
class test_01UserLoginByPwdTestCase(unittest.TestCase):
    # 医生登录
    excel = HandleExcel(filename, "UserLoginByPwd")
    cases = excel.read_data()

    @data(*cases)
    def test_UserLoginByPwd(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        # 调用接口,获取实际结果
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
class test_02getDoctorInfoTestCase(unittest.TestCase):
    # 获取医生的问诊信息
    excel = HandleExcel(filename, "getDoctorInfo")
    cases = excel.read_data()

    @data(*cases)
    def test_getDoctorInfo(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        # 调用接口,获取实际结果
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
class test_03syncAppointmentListTestCase(unittest.TestCase):
    # 获取待接诊人员列表
    excel = HandleExcel(filename, "syncAppointmentList")
    cases = excel.read_data()

    @data(*cases)
    def test_syncAppointmentList(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        # 调用接口,获取实际结果
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
class test_04changeDoctorWorkStateTestCase(unittest.TestCase):
    # 更新医生工作状态
    excel = HandleExcel(filename, "changeDoctorWorkState")
    cases = excel.read_data()

    @data(*cases)
    def test_changeDoctorWorkState(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        # 调用接口,获取实际结果
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
class test_05createChatRoomTestCase(unittest.TestCase):
    # 创建房间
    excel = HandleExcel(filename, "createChatRoom")
    cases = excel.read_data()

    @data(*cases)
    def test_createChatRoom(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        # 调用接口,获取实际结果
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
class test_06syncAppointmentInfoTestCase(unittest.TestCase):
    # 修改问诊的预约状态
    excel = HandleExcel(filename, "syncAppointmentInfo")
    cases = excel.read_data()

    @data(*cases)
    def test_syncAppointmentInfo(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        # 调用接口,获取实际结果
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
class test_07getDrugInfoByNameTestCase(unittest.TestCase):
    # 修改问诊的预约状态
    excel = HandleExcel(filename, "getDrugInfoByName")
    cases = excel.read_data()

    @data(*cases)
    def test_getDrugInfoByName(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        # 调用接口,获取实际结果
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
class test_08getPasteListTestCase(unittest.TestCase):
    # 修改问诊的预约状态
    excel = HandleExcel(filename, "getPasteList")
    cases = excel.read_data()

    @data(*cases)
    def test_getPasteList(self, case):
        # 准备用例数据
        url = "https://doctor.yy365.cn/ComHandle/getPasteList"
        method = "post"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {"QueryType": "", "Params": '{"search":""}',
                "UserGuid": "MTg2OTkwfEA5Yzg0MWM4ZThmNzdjY2FhYjAwZTg2MDY2MmZmNDNjM3xAN2E2ZmQ0ZmRkOWRjYTRlZGQ4NzRiNmUzNjEzNmExOGU-"}
        res = request(url=url, method=method, data=data, headers=headers, verify=False)
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        # 调用接口,获取实际结果
        try:
            self.assertEqual(expected["status_code"], res.status_code)
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