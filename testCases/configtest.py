from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


# @pytest.fixture()
# def setup():
#     obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver.exe")
#     driver = webdriver.Chrome(service=obj)
#     return driver
# @pytest.fixture()
# def setup(browser):
#     if browser=='chrome':
#         driver=webdriver.Chrome()
#     elif browser=='firefox':
#         driver = webdriver.Firefox()
#     else:
#         driver = webdriver.Chrome()
#     return driver

# def pytest_addoption(parser): #get the value from CLI /hooks
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request): #return the browser value to setup method
#     return request.config.getoption("--browser")

# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser", action="store", default="chrome", help="Choose browser: chrome or firefox"
#     )
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")

# def pytest_configure(config):
#     config.metadata['Project Name'] = 'Ecom Website'
#     config.metadata['Module Name'] = 'Customers'
#     config.metadata['Tester'] = 'Japan'
#
# def pytest_metadata(metadata):
#     metadata.pop("Java_Home",None)
#     metadata.pop("Plugins",None)