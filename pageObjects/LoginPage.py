from selenium.webdriver.common.by import By

class Login:
        textbox_username_id = "user-name"
        textbox_password_id = "password"
        button_login_xpath = "//*[@id='login-button']"
        logout_menu = "//*[@id='react-burger-menu-btn']"
        logout_xpath = "//*[@id='logout_sidebar_link']"

        def __init__(self,driver):
            self.driver = driver

        def set_username(self, username):
            self.driver.find_element(By.ID, self.textbox_username_id).clear()
            self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

        def set_password(self, password):
            self.driver.find_element(By.ID, self.textbox_password_id).clear()
            self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

        def click_login(self):
            self.driver.find_element(By.XPATH, self.button_login_xpath).click()

        def click_logout(self):
            self.driver.find_element(By.XPATH,self.logout_menu).click()
            self.driver.find_element(By.XPATH, self.logout_xpath).click()