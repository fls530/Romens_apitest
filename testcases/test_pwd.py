import os
import unittest
from common.handle_excel import HandleExcel
from library.myddt import ddt, data
from common.handle_config import conf
from requests import request
from common.handle_logging import log
from common.handle_path import DATA_DIR
from common.handle_data import EnvData, replace_data

filename = os.path.join(DATA_DIR, "testcase.xlsx")


@ddt
class OrgguidTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "PWD")
    cases = excel.read_data()

    @data(*cases)
    def test_orgguid(self, case):
        # 准备用例数据
        method = case["method"]
        headers = eval(conf.get("env", "headers"))
        url = conf.get("env", "url") + case["url"]
        data = eval(replace_data(case["data"]))
        expected = eval(case["expected"])

        expectedResult = ''
        if 'result' in expected:
            expectedResult = expected['result']
        elif 'ERROR' in expected:
            expectedResult = expected['ERROR']
        row = case["case_id"] + 1
        # 调用接口,获取实际结果
        res = (request(url=url, method=method, data=data, headers=headers)).json()
        try:
            result = ''
            if 'result' in res:
                result = res['result']
            elif 'ERROR' in res:
                result = res['ERROR']
            self.assertEqual(expectedResult, result)
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
