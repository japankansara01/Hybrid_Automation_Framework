from selenium.webdriver.common.by import By

class AddtoCart:

    bag_button = "//*[@id='add-to-cart-sauce-labs-backpack']"
    tshirt_buttton = "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    cart_button = "//*[@id='shopping_cart_container']/a"
    checkout_buttton = "//*[@id='checkout']"

    def __init__(self, driver):
        self.driver = driver

    def click_bagbtn(self):
        self.driver.find_element(By.XPATH, self.bag_button).click()

    def click_tshirtbtn(self):
        self.driver.find_element(By.XPATH, self.tshirt_buttton).click()

    def click_cartbtn(self):
        self.driver.find_element(By.XPATH, self.cart_button).click()

    def click_checkoutbtn(self):
        self.driver.find_element(By.XPATH, self.checkout_buttton).click()