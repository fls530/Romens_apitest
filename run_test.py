import unittest
from common.BE import BE
from common.handle_logging import log
from common.handle_path import CASE_DIR, REPORT_DIR
from common.ding_talk import DingTalkSend
from common.handle_config import conf
import time

log.info("---------------开始执行测试用例-----------------------")

# 创建测试套件
suite = unittest.TestSuite()

# 加载用例到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASE_DIR))

# 执行用例生成报告
bf = BE(suite)

ticks = time.strftime("%Y%m%d%H%M%S", time.localtime())
filename = str(ticks) + ".html"

bf.report("掌上医馆1.0自动化项目", filename=filename, report_dir=REPORT_DIR)
url = conf.get("env", "base_url") + "Romens_apitest/reports/" + filename
DingTalkSend(url)

log.info("---------------测试用例执行完毕,正在发送报告前往钉钉,请注意查收-----------------------")
