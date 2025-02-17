import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import Login
from testCases.configtest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtil

class TestDdtLogin002:
    baseURL = ReadConfig.get_url()
    path=".//TestData/LoginData.xlsx"
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homepagetitle(self,setup):
        self.logger.info("*************Test_002_DDT_Login*************")
        self.logger.info("*************Verifying Home Page Title*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        actualtitle = self.driver.title

        if actualtitle == "Swag Labs":
            assert True
            self.driver.close()
            self.logger.info("*************Home page title test passed*************")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*************Home page title test failed*************")
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login_dd(self,setup):
        self.logger.info("*************Verifying login test*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = Login(self.driver)

        self.rows = ExcelUtil.get_rowcount(self.path,"Sheet1")

        lst_status = []
        self.driver.implicitly_wait(5)

        for r in range(2, self.rows+1):
            self.user = ExcelUtil.read_data(self.path,"Sheet1",r,1)
            self.password = ExcelUtil.read_data(self.path,"Sheet1",r,2)
            self.exp = ExcelUtil.read_data(self.path,"Sheet1",r,3)

            # Added a check to skip iteration if username or password is None to avoid TypeError during login.
            if self.user is None or self.password is None:
                self.logger.error(f"Missing credentials for row {r}: username={self.user}, password={self.password}")
                continue

            self.login.set_username(self.user)
            self.login.set_password(self.password)
            self.login.click_login()

            try:
                # Find element as title of login and dashboard is same
                dashboard_element = self.driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a") # Cart XPATH to validate login
                act_status = "Pass"  # Login is successful if the element is found
            except:
                act_status = "Fail"

            if act_status=="Pass":
                if self.exp=="Pass":
                    self.logger.info("***passed***")
                    self.login.click_logout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("***failed***")
                    lst_status.append("Fail")
            elif act_status == "Fail":
                if self.exp=="Pass":
                    self.logger.info("***failed***")
                    lst_status.append("Fail")
                elif self.exp=="fail":
                    self.logger.info("***passed***")
                    lst_status.append("Pass")

            # self.logger.info(f"Status list: {lst_status}")
        if "Fail" in lst_status:
            self.logger.info("***Test case failed***")
            assert False
        else:
            self.logger.info("***Test case Passed***")
            assert True
        self.logger.info("***End of Login DD Test***")