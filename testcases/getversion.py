import os
import unittest
from common.handle_excel import HandleExcel
from library.myddt import ddt, data
from common.handle_config import conf
from requests import request
from common.handle_logging import log
from common.handle_path import DATA_DIR
from common.handle_data import EnvData, replace_data, login

filename = os.path.join(DATA_DIR, "testcase.xlsx")


@ddt
class OrgguidTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "getversion")
    cases = excel.read_data()

    @data(*cases)
    def test_getversion(self, case):
        method = case["method"]
        headers = eval(conf.get("env", "headers"))
        url = conf.get("env", "url") + case["url"]
        dic1 = eval(case["data"])
        dic1["UserGuid"] = login()
        data = replace_data(dic1)
        expected = eval(case["expected"])
        res = (request(url=url, method=method, data=data, headers=headers)).json()
        print(res)
