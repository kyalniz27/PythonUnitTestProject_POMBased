from selenium.webdriver.common.by import By

class LoginPage():
    user = '#txtUsername'
    password = '#txtPassword'
    loginBtn = '#btnLogin'
    userName = '#welcome'
    logoutBtn = "a[href='/index.php/auth/logout']"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,userEmail):
        self.driver.find_element(By.CSS_SELECTOR,self.user).send_keys(userEmail)

    def setPassword(self,userPassword):
        self.driver.find_element(By.CSS_SELECTOR,self.password).send_keys(userPassword)

    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR,self.loginBtn).click()

    def clickLogOut(self):
        self.driver.find_element(By.CSS_SELECTOR,self.userName).click()
        self.driver.find_element(By.CSS_SELECTOR,self.logoutBtn).click()