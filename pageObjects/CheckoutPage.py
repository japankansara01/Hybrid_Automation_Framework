from selenium.webdriver.common.by import By

class Checkout:

    txtfirstname_xpath = "//*[@id='first-name']"
    txtlastname_xpath = "//*[@id='last-name']"
    zipcode_xpath = "//*[@id='postal-code']"
    continue_xpath = "//*[@id='continue']"

    def __init__(self, driver):
        self.driver = driver

    def setfirstname(self, firstname):
        self.driver.find_element(By.XPATH, self.txtfirstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtfirstname_xpath).send_keys(firstname)

    def setlastname(self,  lastname):
        self.driver.find_element(By.XPATH, self.txtlastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtlastname_xpath).send_keys(lastname)

    def setzip(self, zipcode):
        self.driver.find_element(By.XPATH, self.zipcode_xpath).clear()
        self.driver.find_element(By.XPATH, self.zipcode_xpath).send_keys(zipcode)

    def click_continue(self):
        self.driver.find_element(By.XPATH, self.continue_xpath).click()