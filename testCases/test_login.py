
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from testCases.configtest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import pytest
class TestLogin001:
    baseURL = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homepagetitle(self,setup):
        self.logger.info("*************Test_001_Login*************")
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
    def test_login(self,setup):
        self.logger.info("*************Verifying login test*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = Login(self.driver)
        self.login.set_username(self.username)
        self.login.set_password(self.password)
        self.login.click_login()
        try:
            # Find element as title of login and dashboard is same
            dashboard_element = self.driver.find_element(By.XPATH,"//*[@id='shopping_cart_container']/a")  # Cart XPATH to validate login
            act_status = "Pass"  # Login is successful if the element is found
        except:
            act_status = "Fail"

        if act_status=="Pass":
            assert True
            self.logger.info("*************Login test passed*************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_login.png")
            self.logger.error("*************Login test failed*************")
            self.driver.close()
            assert False