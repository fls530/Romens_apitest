import base64
import json
import re
import jsonpath
from common.handle_config import conf
from requests import request
import datetime
import warnings

warnings.filterwarnings("ignore")


class EnvData:
    """定义一个类，用来保存用例执行过程中，提取出来的数据（当成环境变量的容器）"""
    pass


def replace_data(data):
    """替换数据"""

    while re.search("#(.*?)#", data):
        res = re.search("#(.*?)#", data)
        # 返回的式一个匹配对象
        # 获取匹配到的数据
        key = res.group()
        # 获取匹配规则中括号里面的内容
        item = res.group(1)
        try:
            # 获取配置文件中对应的值
            value = conf.get("test_data", item)
        except BaseException:
            # 去EnvData这个类里面获取对应的属性（环境变量）
            value = getattr(EnvData, item)
        data = data.replace(key, value)
    return data


def login():
    method = 'post'
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    url = 'http://doctor.yy365.cn/Login'
    data = {"QueryType": "userLoginInByPwd",
            "Params": '{"DEVICEID": "' + conf.get("test_data", "DEVICEID") + '", '
                                                                             '"USERPHONE": "' +
                      conf.get("test_data", "USERPHONE") + '", '
                                                           '"PWD": "000000", "ORGGUID": "' +
                      conf.get("test_data", "ORGGUID") + '",'
                                                         '"AppName": "com.romens.health.pharmacy.client"}'}
    res = (request(url=url, method=method, data=data, headers=headers)).json()
    try:
        dic = {"ORG_CODE": conf.get("test_data", "ORGGUID"),
               "SHOP_CODE": jsonpath.jsonpath(res, "$..shopCode")[0],
               "USER_CODE": conf.get("test_data", "USERPHONE"),
               "USER_PASSWORD": jsonpath.jsonpath(res, "$..token")[0],
               "APP_VERSION": conf.get("test_data", "APP_VERSION"),
               "APP_KEY": conf.get("test_data", "APP_KEY"),
               "PACKAGE_NAME": conf.get("test_data", "PACKAGE_NAME"),
               "CHILD_ID": jsonpath.jsonpath(res, "$..childId")[0],
               "SIGN": jsonpath.jsonpath(res, "$..sign")[0]}
        token = "@@" + bytes.decode(base64.b64encode(json.dumps(dic).
                                                     encode('utf-8'))).replace('=', '-').replace('+', '_')
    except Exception as e:
        raise e
    return token


def getdata(case):
    method = case["method"]
    headers = eval(conf.get("env", "headers"))
    url = conf.get("env", "url") + case["url"]
    data = eval(replace_data(case["data"]))
    row = case["case_id"] + 1
    expected = eval(case["expected"])
    expectedResult = ''
    if 'result' in expected:
        expectedResult = expected['result']
    elif 'ERROR' in expected:
        expectedResult = expected['ERROR']
    expected = expectedResult

    return method, headers, url, data, row, expected


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday
