from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture()
def setup():
    obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=obj)
    return driver

# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")

def pytest_configure(config):
    config.metadata['Project Name'] = 'Ecom Website'
    config.metadata['Module Name'] = 'Customers'
    config.metadata['Tester'] = 'Japan'

def pytest_metadata(metadata):
    metadata.pop("Java_Home",None)
    metadata.pop("Plugins",None)

# def pytest_configure(config):
#     # Add metadata to the report
#     config._metadata['Project Name'] = 'Ecom Website'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'abc'
#
# # Optional: If you want to remove Java_Home or Plugins from metadata
# def pytest_html_results_summary(prefix, summary, postfix):
#     summary.append("<p><strong>Project Name:</strong> Ecom Website</p>")
#     summary.append("<p><strong>Module Name:</strong> Customers</p>")
#     summary.append("<p><strong>Tester:</strong> Japan</p>")
