import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from testCases.configtest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtil

class Test_002_DDT_Login:
    baseURL = ReadConfig.get_url()
    path=".//TestData/LoginData.xlsx"
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("*************Test_002_DDT_Login*************")
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

    def test_login_dd(self,setup):
        self.logger.info("*************Verifying login test*************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.rows = ExcelUtil.getRowCount(self.path,"Sheet1")

        lst_status = []

        for r in range(2, self.rows+1):
            self.user = ExcelUtil.readData(self.path,"Sheet1",r,1)
            self.password = ExcelUtil.readData(self.path,"Sheet1",r,2)
            self.exp = ExcelUtil.readData(self.path,"Sheet1",r,3)

            self.login.setUserName(self.user)
            self.login.setPassword(self.password)
            self.login.clickLogin()
            time.sleep(5)

            actTitle = self.driver.title
            expTitle = "Swag Labs"

            if actTitle==expTitle:
                if self.exp=="pass":
                    self.logger.info("***Passed***")
                    self.login.clickLogout()
                    lst_status.append("pass")
                elif self.exp=="fail":
                    self.logger.info("***failed***")
                    self.login.clickLogout()
                    lst_status.append("fail")
            elif actTitle==expTitle:
                if self.exp=="pass":
                    self.logger.info("***Failed***")
                    self.login.clickLogout()
                    lst_status.append("fail")
                elif self.exp=="fail":
                    self.logger.info("***passed***")
                    self.login.clickLogout()
                    lst_status.append("pass")

            if "Fail" not in lst_status:
                self.logger.info("***Test case passed***")
                assert True
            else:
                self.logger.info("***Test case failed***")
                assert False
        self.logger.info("***End of Login DD Test***")
