import os
import unittest
from common.handle_excel import HandleExcel
from library.myddt import ddt, data
from requests import request
from common.handle_logging import log
from common.handle_path import DATA_DIR
from common.handle_data import login, getdata

filename = os.path.join(DATA_DIR, "system.xlsx")


@ddt
class test_01OrgguidTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "ORGGUID")
    cases = excel.read_data()

    @data(*cases)
    def test_orgguid(self, case):
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
class test_02PhoneTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "PHONE")
    cases = excel.read_data()

    @data(*cases)
    def test_phone(self, case):
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
class test_03PwdTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "PWD")
    cases = excel.read_data()

    @data(*cases)
    def test_pwd(self, case):
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
            result = ''
            if 'result' in res:
                result = res['result']
            elif 'ERROR' in res:
                result = res['ERROR']
            self.assertEqual(expected, result)
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
class test_04GetversionTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getversion")
    cases = excel.read_data()

    @data(*cases)
    def test_getversion(self, case):
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
class test_05getFileUploadParamsTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getFileUploadParams")
    cases = excel.read_data()

    @data(*cases)
    def test_getparams(self, case):
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
class test_06getTxCosConfigTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getTxCosConfig")
    cases = excel.read_data()

    @data(*cases)
    def test_getconfig(self, case):
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
class test_07syncSysConfigTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "syncSysConfig")
    cases = excel.read_data()

    @data(*cases)
    def test_syncSysConfig(self, case):
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
class test_08getConfigTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getConfig")
    cases = excel.read_data()

    @data(*cases)
    def test_getConfig(self, case):
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
class test_09getAppTitleTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getAppTitle")
    cases = excel.read_data()

    @data(*cases)
    def test_getAppTitle(self, case):
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
