import pytest
import allure

# Severity：严重级别(BLOCKER,CRITICAL,NORMAL,MINOR,TRIVIAL)

class Test01():
    @allure.step(title="开始")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test001(self):
        print("test001被执行")

    @allure.step(title="结束")
    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test002(self):
        allure.attach("描述","test001开始执行了")
        print("test001被执行")

    @allure.step(title="结束")
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test003(self):
        allure.attach("描述","test003开始执行了")
        with open("./image/Snipaste.png","rb") as f:
            allure.attach("图片",f.read(),allure.attach_type.PNG)
        print("test003被执行")
