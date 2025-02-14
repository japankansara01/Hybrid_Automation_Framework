import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from testCases.configtest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("*************Test_001_Login*************")
        self.logger.info("*************Verifying Home Page Title*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        actualTitle = self.driver.title

        if actualTitle == "Swag Labs":
            assert True
            self.driver.close()
            self.logger.info("*************Home page title test passed*************")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*************Home page title test failed*************")
            assert False

    def test_login(self,setup):
        self.logger.info("*************Verifying login test*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = Login(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        actualTitle = self.driver.title

        if actualTitle == "Swag Labs":
            assert True
            self.logger.info("*************Login test passed*************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_login.png")
            self.logger.error("*************Login test failed*************")
            self.driver.close()
            assert False