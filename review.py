import time
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
desired_caps['appPackage'] = 'com.vcooline.aike'
desired_caps['appActivity'] = '.umanager.LoginActivity'
# 获取driver
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.close_app()
driver.start_activity("com.vcooline.aike",".umanager.LoginActivity")
driver.close_app()
# 判断爱克是否安装，安装则卸载，如果未安装，则进行安装
#
# driver.quit()
