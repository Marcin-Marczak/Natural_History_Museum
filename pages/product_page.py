from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.quantity = (By.XPATH, "//input[@class='input-text qty']")
        self.update_basket = (By.XPATH, "//button[@title = 'Update Basket']")
        self.product_name = (By.XPATH, "//span[@class='base']")
        self.add_to_basket_button = (By.XPATH, "//button[@title='Add to basket']")
        self.shopping_basket_link = (By.LINK_TEXT, "shopping basket")

    def change_product_quantity_on_product_page(self):
        self.driver.find_element(*self.quantity).click()
        time.sleep(3)
        webdriver.ActionChains(self.driver).send_keys(Keys.DELETE).perform()
        time.sleep(3)
        self.driver.find_element(*self.quantity).send_keys("2")
        time.sleep(3)
        self.driver.find_element(*self.update_basket).click()
        time.sleep(5)

    def get_name_of_product_on_product_page(self):
        return self.driver.find_element(*self.product_name).text

    def add_product_to_basket_on_product_page_and_go_to_basket(self):
        self.driver.find_element(*self.add_to_basket_button).click()
        self.driver.find_element(*self.shopping_basket_link).click()
        WebDriverWait(self.driver, 10).until(ec.url_changes)