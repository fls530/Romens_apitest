import os
import unittest
from common.handle_excel import HandleExcel
from library.myddt import ddt, data
from requests import request
from common.handle_logging import log
from common.handle_path import DATA_DIR
from common.handle_data import getdata, login

filename = os.path.join(DATA_DIR, "remote.xlsx")


@ddt
class test_01searchMemberTestCase(unittest.TestCase):
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
                headers=headers)).json()
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
    excel = HandleExcel(filename, "syncUserOrderCode")
    cases = excel.read_data()

    @data(*cases)
    def test_syncUserOrderCode(self, case):
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
        res = (
            request(
                url=url,
                method=method,
                data=data,
                headers=headers)).json()
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
    excel = HandleExcel(filename, "getUserVisitTemplates")
    cases = excel.read_data()

    @data(*cases)
    def test_getUserVisitTemplates(self, case):
        method, headers, url, data, row, expected = getdata(case)
        data["UserGuid"] = login()
        res = (
            request(
                url=url,
                method=method,
                data=data,
                headers=headers)).json()
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
            request(
                url=url,
                method=method,
                data=data,
                headers=headers)).json()
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