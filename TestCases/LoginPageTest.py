import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
sys.path.append("C://Users//seker//PycharmProjects//PythonUnitTestProject_POMBased")
from PageObjects.LoginPage import LoginPage
from time import sleep

class LoginTest(unittest.TestCase):
    baseURL = "https://opensource-demo.orangehrmlive.com"
    username = "Admin"
    password = "admin123"
    driver = webdriver.Firefox(executable_path="C://Users//seker//PycharmProjects//PythonUnitTestProject_POMBased//Driver//geckodriver.exe")

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.setEmail(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        lp.clickLogOut()
        sleep(5)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C://Users//seker//PycharmProjects//PythonUnitTestProject_POMBased//Reports'))


