import unittest
from BeautifulReport import BeautifulReport
from common.handle_logging import log
from common.handle_path import CASE_DIR, REPORT_DIR

log.info("---------------开始执行测试用例-----------------------")

# 创建测试套件
suite = unittest.TestSuite()

# 加载用例到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASE_DIR))

# 执行用例生成报告
bf = BeautifulReport(suite)

bf.report("接口自动化", filename="report.html", report_dir=REPORT_DIR)

log.info("---------------测试用例执行完毕,正在发送邮件,请注意查收-----------------------")