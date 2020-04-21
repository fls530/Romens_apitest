import os
import unittest
import random
from common.handle_excel import HandleExcel
from library.myddt import ddt, data
from common.handle_config import conf
from requests import request
from common.handle_logging import log
from common.handle_path import DATA_DIR

filename = os.path.join(DATA_DIR, "testcase.xlsx")


@ddt
class OrgguidTestCase(unittest.TestCase):
    excel = HandleExcel(filename, "ORGGUID")
    cases = excel.read_data()

    @data(*cases)
    def test_orgguid(self, case):
        # 准备用例数据
        method = case["method"]




