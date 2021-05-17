import os
import unittest
from common.handle_config import conf
from common.handle_excel import HandleExcel
from library.myddt import ddt, data
from requests import request, Session
from common.handle_logging import log
from common.handle_path import DATA_DIR
from common.handle_data import getdata

filename = os.path.join(DATA_DIR, "shopweb.xlsx")


@ddt
# 门店登录
class test_01LoginTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "login")
    cases = excel.read_data()

    @data(*cases)
    def test_Login(self, case):
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
# 获取处方单列表
class test_02getDataListTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getDataList")
    cases = excel.read_data()

    @data(*cases)
    def test_getDataList(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "shop_user"),
            "password": conf.get("test_data", "shop_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["draw"], res["draw"])
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
# 查看视频记录
class test_03getChatVedioTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getChatVedio")
    cases = excel.read_data()

    @data(*cases)
    def test_getChatVedio(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "shop_user"),
            "password": conf.get("test_data", "shop_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["CODE"], res["CODE"])
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
# 获取处方数据
class test_04getOrderTempleDataTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getOrderTempleData")
    cases = excel.read_data()

    @data(*cases)
    def test_getOrderTempleData(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "shop_user"),
            "password": conf.get("test_data", "shop_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["ORGGUID"], res["ORGGUID"])
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
# 获取处方数据
class test_05getOrderTempleDataTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getOrderTempleData")
    cases = excel.read_data()

    @data(*cases)
    def test_getOrderTempleData(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "shop_user"),
            "password": conf.get("test_data", "shop_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["ORGGUID"], res["ORGGUID"])
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
# 获取待确认问诊列表
class test_06getOrderListTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getOrderList")
    cases = excel.read_data()

    @data(*cases)
    def test_getOrderList(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "shop_user"),
            "password": conf.get("test_data", "shop_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["draw"], res["draw"])
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
# 提交处方
class test_07saveOfflineOrderTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "saveOfflineOrder")
    cases = excel.read_data()

    @data(*cases)
    def test_saveOfflineOrder(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "shop_user"),
            "password": conf.get("test_data", "shop_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["CODE"], res["CODE"])
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
# 外来处方-待审核处方
class test_08getDataList1TestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getDataList1")
    cases = excel.read_data()

    @data(*cases)
    def test_getDataList1(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "shop_user"),
            "password": conf.get("test_data", "shop_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["draw"], res["draw"])
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
# 获取处方详情
class test_09getOfflineOrderInfoTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getOfflineOrderInfo")
    cases = excel.read_data()

    @data(*cases)
    def test_getOfflineOrderInfo(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "shop_user"),
            "password": conf.get("test_data", "shop_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["CODE"], res["CODE"])
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
# 获取挂单列表
class test_10getDataList2TestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getDataList2")
    cases = excel.read_data()

    @data(*cases)
    def test_getDataList2(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "shop_user"),
            "password": conf.get("test_data", "shop_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["Code"], res["Code"])
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
