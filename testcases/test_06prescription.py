import os
import unittest
import jsonpath
from common.handle_config import conf
from common.handle_excel import HandleExcel
from library.myddt import ddt, data
from requests import request
from common.handle_logging import log
from common.handle_path import DATA_DIR
from common.handle_data import login, getdata, EnvData, getYesterday

filename = os.path.join(DATA_DIR, "prescription.xlsx")


@ddt
class test_01getMedicationInterTestCase(unittest.TestCase):
    # 获取处方上传输入模板
    excel = HandleExcel(filename, "getMedicationInter")
    cases = excel.read_data()

    @data(*cases)
    def test_getMedicationInter(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
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
class test_02getConfigTestCase(unittest.TestCase):
    # 获取配置
    excel = HandleExcel(filename, "getConfig")
    cases = excel.read_data()

    @data(*cases)
    def test_getConfig(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
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
class test_03getDrugListTestCase(unittest.TestCase):
    # 搜索药品
    excel = HandleExcel(filename, "getDrugList")
    cases = excel.read_data()

    @data(*cases)
    def test_getDrugList(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
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
class test_04ordonUploadTestCase(unittest.TestCase):
    # 上传处方
    excel = HandleExcel(filename, "ordonUpload")
    cases = excel.read_data()

    @data(*cases)
    def test_ordonUpload(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
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
class test_05getOnlineOrderTestCase(unittest.TestCase):
    # 线上处方列表
    excel = HandleExcel(filename, "getOnlineOrder")
    cases = excel.read_data()

    @data(*cases)
    def test_getOnlineOrder(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
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
class test_06getPrescriptListTestCase(unittest.TestCase):
    # 获取今日外方处方单列表
    excel = HandleExcel(filename, "getPrescriptList")
    cases = excel.read_data()

    @data(*cases)
    def test_getPrescriptList(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
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
class test_07getHisPrescriptTestCase(unittest.TestCase):
    # 获取历史处方列表
    excel = HandleExcel(filename, "getHisPrescript")
    cases = excel.read_data()
    EnvData.yesterday = str(getYesterday())

    @data(*cases)
    def test_getHisPrescript(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
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
class test_08getShopLoginInfoTestCase(unittest.TestCase):
    # 获取门店子账号信息
    excel = HandleExcel(filename, "getShopLoginInfo")
    cases = excel.read_data()

    @data(*cases)
    def test_getShopLoginInfo(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
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
class test_09getAllShopTestCase(unittest.TestCase):
    # 申请调店
    excel = HandleExcel(filename, "getAllShop")
    cases = excel.read_data()

    @data(*cases)
    def test_getAllShop(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
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
class test_10shopApplyTestCase(unittest.TestCase):
    # 申请调店
    excel = HandleExcel(filename, "shopApply")
    cases = excel.read_data()

    @data(*cases)
    def test_shopApply(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
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
class test_11saveShopLoginSignUrlTestCase(unittest.TestCase):
    # 申请调店
    excel = HandleExcel(filename, "saveShopLoginSignUrl")
    cases = excel.read_data()

    @data(*cases)
    def test_saveShopLoginSignUrl(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
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
class test_12saveOrderSignUrlTestCase(unittest.TestCase):
    # 线上处方单调配、复合发药片
    excel = HandleExcel(filename, "saveOrderSignUrl")
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        # 前置条件1:请求会员查询接口获取会员编号,设置为类属性
        url = conf.get("env", "url") + "/Inquiry"
        method = "post"
        headers = eval(conf.get("env", "headers"))
        data = {"QueryType": "getOnlineOrder", "Params": '{"page":0}', "UserGuid": login()}
        res = (request(url=url, method=method, data=data, headers=headers, verify=False)).json()
        # 提取会员编号作为类属性
        # EnvData.guid = jsonpath.jsonpath(res, "$..ID")[0]

    @data(*cases)
    def test_saveOrderSignUrl(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
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
class test_13saveOfflineSignUrlTestCase(unittest.TestCase):
    # 线下处方单调配、复合发药片
    excel = HandleExcel(filename, "saveOfflineSignUrl")
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        # 前置条件1:请求会员查询接口获取会员编号,设置为类属性
        url = conf.get("env", "url") + "/Inquiry"
        method = "post"
        headers = eval(conf.get("env", "headers"))
        data = {"QueryType": "getPrescriptList", "Params": '{"orderCode":"","page":1,"status":""}', "UserGuid": login()}
        res = (request(url=url, method=method, data=data, headers=headers, verify=False)).json()
        # 提取会员编号作为类属性
        EnvData.guid = jsonpath.jsonpath(res, "$..ORDERCODE")[0]

    @data(*cases)
    def test_saveOfflineSignUrl(self, case):
        # 准备用例数据
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
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
