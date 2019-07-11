import os
import sys
sys.path.append(os.getcwd())
from tool.read_yaml import read_yaml
from page.page_login import PageLogin
import pytest


def get_data():
    arrs = []
    for data in read_yaml().values():
        arrs.append((data.get("username"), data.get("pwd")))
    return arrs


class TestLogin(object):
    # 初始化
    def setup_class(self):
        # 实例化PageLogin
        self.login = PageLogin()

    # 结束
    def teardown_class(self):
        self.login.driver.quit()

    # 登录测试方法
    @pytest.mark.parametrize("phone,pwd", get_data())
    def test_login(self, phone, pwd):
        # 调用登录业务方法
        self.login.page_login(phone, pwd)
