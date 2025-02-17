import time
import pytest
import random
import string
from selenium.webdriver.common.by import By

from testCases.configtest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import Login

from pageObjects.CheckoutPage import Checkout
from pageObjects.HomePage import AddtoCart

def generate_random_fname():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=6))

def generate_random_lname():
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))

def generate_random_pin():
    return random.randint(100000, 999999)

class TestCheckout003:
    baseURL = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    logger = LogGen.loggen()


    def test_checkout(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.logger.info("*************Test_003_Checkout*************")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.login = Login(self.driver)
        self.login.set_username(self.username)
        self.login.set_password(self.password)
        self.login.click_login()
        self.logger.info("*************Login successful*************")

        self.checkout = AddtoCart(self.driver)
        self.checkout.click_bagbtn()
        self.checkout.click_tshirtbtn()
        self.checkout.click_cartbtn()
        self.checkout.click_checkoutbtn()
        self.logger.info("*************Items Added in cart successfully*************")

        self.checkout_info = Checkout(self.driver)
        self.firstname = generate_random_fname()
        self.lastname = generate_random_lname()
        self.zipcode = generate_random_pin()

        self.checkout_info.setfirstname(self.firstname)
        self.checkout_info.setlastname(self.lastname)
        self.checkout_info.setzip(self.zipcode)
        self.checkout_info.click_continue()
        self.logger.info("*************Information added successfully*************")

        self.total = self.driver.find_element(By.XPATH,"//*[@id='checkout_summary_container']/div/div[2]/div[8]").text
        print("Total amount in cart: ", self.total)

        self.finish_btn = self.driver.find_element(By.XPATH,"//*[@id='finish']").click()
        time.sleep(3)