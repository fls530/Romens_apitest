import os
import unittest
from common.handle_config import conf
from common.handle_excel import HandleExcel
from library.myddt import ddt, data
from requests import request, Session
from common.handle_logging import log
from common.handle_path import DATA_DIR
from common.handle_data import getdata

filename = os.path.join(DATA_DIR, "pharmacist.xlsx")


@ddt
# 药师登录
class test_01LoginTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "Login")
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
# 判断是否开启人脸验证
class test_02checkPharCompareFaceTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "checkPharCompareFace")
    cases = excel.read_data()

    @data(*cases)
    def test_checkPharCompareFace(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "phar_user"),
            "password": conf.get("test_data", "phar_pwd")}
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
# 保存药师人脸信息
class test_03savePharImgTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "savePharImg")
    cases = excel.read_data()

    @data(*cases)
    def test_savePharImg(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "phar_user"),
            "password": conf.get("test_data", "phar_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["CODE"], res["DATA"]['CODE'])
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
# 获取药师工作状态
class test_04getWorkStateTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getWorkState")
    cases = excel.read_data()

    @data(*cases)
    def test_getWorkState(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "phar_user"),
            "password": conf.get("test_data", "phar_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        response2 = se.post(url=url1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["CODE"], res['CODE'])
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
# 设置药师工作状态
class test_05setPharWorkStateTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "setPharWorkState")
    cases = excel.read_data()

    @data(*cases)
    def test_setPharWorkState(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "phar_user"),
            "password": conf.get("test_data", "phar_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["CODE"], res['CODE'])
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
# 获取药师审方列表
class test_06getDataListTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getDataList")
    cases = excel.read_data()

    @data(*cases)
    def test_getDataList(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "phar_user"),
            "password": conf.get("test_data", "phar_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["draw"], res['draw'])
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
# 验证药师审核密码
class test_07checkPwdTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "checkPwd")
    cases = excel.read_data()

    @data(*cases)
    def test_checkPwd(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "phar_user"),
            "password": conf.get("test_data", "phar_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["CODE"], res['CODE'])
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
# 获取历史处方
class test_08gethistoryDataListTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "gethistoryDataList")
    cases = excel.read_data()

    @data(*cases)
    def test_gethistoryDataList(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "phar_user"),
            "password": conf.get("test_data", "phar_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["draw"], res['draw'])
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
# 获取药师待审核处方列表
class test_09getnoapprovedListTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "noapproved")
    cases = excel.read_data()

    @data(*cases)
    def test_getnoapprovedList(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "phar_user"),
            "password": conf.get("test_data", "phar_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["draw"], res['draw'])
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
# 获取药师已审核处方列表
class test_10getapprovedListTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "approved")
    cases = excel.read_data()

    @data(*cases)
    def test_getapprovedList(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "phar_user"),
            "password": conf.get("test_data", "phar_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["draw"], res['draw'])
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
class test_11getOfflineOrderInfoTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getOfflineOrderInfo")
    cases = excel.read_data()

    @data(*cases)
    def test_getOfflineOrderInfo(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "phar_user"),
            "password": conf.get("test_data", "phar_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["CODE"], res['CODE'])
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
# 获取用药咨询列表(实时列表)
class test_12getMedicationInterTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getMedicationInter")
    cases = excel.read_data()

    @data(*cases)
    def test_getMedicationInter(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "phar_user"),
            "password": conf.get("test_data", "phar_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["draw"], res['draw'])
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
# 获取用药咨询列表(历史列表)
class test_13getMedicationHistoryTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getMedicationHistory")
    cases = excel.read_data()

    @data(*cases)
    def test_getMedicationHistory(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "phar_user"),
            "password": conf.get("test_data", "phar_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["draw"], res['draw'])
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
# 获取用药咨询视频
class test_14getChatVideoTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getChatVideo")
    cases = excel.read_data()

    @data(*cases)
    def test_getChatVideo(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "phar_user"),
            "password": conf.get("test_data", "phar_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["CODE"], res['CODE'])
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
# 接听用药咨询视频（获取用药咨询详细信息）
class test_14syncAppointmentInfoTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "syncAppointmentInfo")
    cases = excel.read_data()

    @data(*cases)
    def test_syncAppointmentInfo(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "phar_user"),
            "password": conf.get("test_data", "phar_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["CODE"], res['CODE'])
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
# 挂断用药咨询视频
class test_15CloseAppointmentTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "CloseAppointment")
    cases = excel.read_data()

    @data(*cases)
    def test_CloseAppointment(self, case):
        se = Session()
        # 准备用例数据
        login_url = "http://doctor.yy365.cn/index/login"
        login_data = {
            "username": conf.get("test_data", "phar_user"),
            "password": conf.get("test_data", "phar_pwd")}
        response = se.post(url=login_url, data=login_data)
        url1 = conf.get("env", "url") + case["url"]
        data1 = eval(case["data"])
        response2 = se.post(url=url1, data=data1, verify=False)
        res = response2.json()
        row = case["case_id"] + 1
        expected = eval(case["expected"])
        try:
            self.assertEqual(expected["CODE"], res['CODE'])
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