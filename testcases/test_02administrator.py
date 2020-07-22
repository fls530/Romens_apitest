import os
import unittest
from common.handle_excel import HandleExcel
from library.myddt import ddt, data
from requests import request
from common.handle_logging import log
from common.handle_path import DATA_DIR
from common.handle_data import login, getdata
from requests.sessions import Session
from common.handle_config import conf

filename = os.path.join(DATA_DIR, "Administrator.xlsx")


@ddt
class test_01loginTestCase(unittest.TestCase):
    # 管理员登陆
    excel = HandleExcel(filename, "login")
    cases = excel.read_data()

    @data(*cases)
    def test_login(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        # 调用接口,获取实际结果
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
class test_02getDataListTestCase(unittest.TestCase):
    # 获取门店列表
    excel = HandleExcel(filename, "getDataList")
    cases = excel.read_data()

    @data(*cases)
    def test_getDataList(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "admin_user"),
            "password": conf.get("test_data", "admin_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = {"params": '{"length":10,"search":'',"start":0,"page":1}'}
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
class test_03importDataTestCase(unittest.TestCase):
    # 导入门店
    excel = HandleExcel(filename, "importData")
    cases = excel.read_data()

    @data(*cases)
    def test_importData(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "admin_user"),
            "password": conf.get("test_data", "admin_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        headers = {"Content-Type": "multipart/form-data"}
        file = {'file': open(r"C:\Users\Administrator\Desktop\Romens_Api_Test\data\891407.xls", 'rb')}
        response2 = se.post(url=url1, files=file, verify=False, headers=headers)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["status_code"], response2.status_code)
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
class test_04getDataListByChildTestCase(unittest.TestCase):
    # 子账号获取
    excel = HandleExcel(filename, "getDataListByChild")
    cases = excel.read_data()

    @data(*cases)
    def test_getDataListByChild(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "admin_user"),
            "password": conf.get("test_data", "admin_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        response2 = se.post(url=url1, verify=False)
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
class test_05getDoctorInfoTestCase(unittest.TestCase):
    # 获取医生列表
    excel = HandleExcel(filename, "getDoctorInfo")
    cases = excel.read_data()

    @data(*cases)
    def test_getDoctorInfo(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "admin_user"),
            "password": conf.get("test_data", "admin_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = {"params": '{"length":10,"search":'',"start":0,"page":1}'}
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
class test_06getlistTestCase(unittest.TestCase):
    # 获取药师列表
    excel = HandleExcel(filename, "getlist")
    cases = excel.read_data()

    @data(*cases)
    def test_getlist(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "admin_user"),
            "password": conf.get("test_data", "admin_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = {"params": '{"length":10,"search":'',"start":0,"page":1}'}
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
class test_07getDataTestCase(unittest.TestCase):
    # 获取处方单列表
    excel = HandleExcel(filename, "getData")
    cases = excel.read_data()

    @data(*cases)
    def test_getData(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "admin_user"),
            "password": conf.get("test_data", "admin_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = {"length": 10, "search": '', "start": 0, "page": 1}
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
class test_08getShopOrderTestCase(unittest.TestCase):
    # 获取门店开方量列表数据
    excel = HandleExcel(filename, "getShopOrder")
    cases = excel.read_data()

    @data(*cases)
    def test_getShopOrder(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "admin_user"),
            "password": conf.get("test_data", "admin_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = {"start": '', "end": '', "shop": 0, "type": 1}
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
class test_09getDoctorOrderTestCase(unittest.TestCase):
    # 获取医生开方量列表
    excel = HandleExcel(filename, "getDoctorOrder")
    cases = excel.read_data()

    @data(*cases)
    def test_getDoctorOrder(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "admin_user"),
            "password": conf.get("test_data", "admin_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = {"start": '', "end": '', "pharmacist": '', "type": 1}
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
class test_10getPharmacistOrderTestCase(unittest.TestCase):
    # 获取药师开方量列表
    excel = HandleExcel(filename, "getPharmacistOrder")
    cases = excel.read_data()

    @data(*cases)
    def test_getPharmacistOrder(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "admin_user"),
            "password": conf.get("test_data", "admin_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = {"start": '', "end": '', "pharmacist": '', "type": 1}
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
class test_11getAppointmentTestCase(unittest.TestCase):
    # 获取预约列表数据
    excel = HandleExcel(filename, "getAppointment")
    cases = excel.read_data()

    @data(*cases)
    def test_getAppointment(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "admin_user"),
            "password": conf.get("test_data", "admin_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        response2 = se.post(url=url1, verify=False)
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
class test_12getGoodsListTestCase(unittest.TestCase):
    # 获取商品列表数据
    excel = HandleExcel(filename, "getGoodsList")
    cases = excel.read_data()

    @data(*cases)
    def test_getGoodsList(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "admin_user"),
            "password": conf.get("test_data", "admin_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = {"start": '', "end": '', "pharmacist": '', "type": 1}
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
