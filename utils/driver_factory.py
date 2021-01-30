from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            return webdriver.Chrome(ChromeDriverManager().install())
        elif browser == "opera":
            return webdriver.Opera(executable_path=OperaDriverManager().install())