from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time


# Notice: Mini basket is shorter and smaller version of basket,
# displayed as a basket icon, located in the top right corner


class MiniBasketPage:

    def __init__(self, driver):
        self.driver = driver
        self.basket_icon = (By.ID, "minicart")
        self.quantity = (By.XPATH, "//input[@data-bind]")
        self.recalculate_quantity = (By.XPATH, "//button[@title='Update']")
        self.remove_product = (By.XPATH, "//a[@title='Remove item']")
        self.confirm_remove_product = (By.XPATH, "//button[@class='action-primary action-accept']")
        self.view_and_edit_basket = (By.XPATH, "//a[@class='action viewcart']")
        self.empty_basket_text = (By.XPATH, "//strong[@class='subtitle empty']")
        self.number_of_items_in_basket = (By.XPATH, "//span[@class='counter-number']")

    def open_mini_basket(self):
        webdriver.ActionChains(self.driver).move_to_element(self.driver.find_element(*self.basket_icon)).perform()
        time.sleep(2)

    def change_quantity_in_mini_basket(self):
        WebDriverWait(self.driver, 10, 0.25).until(ec.element_to_be_clickable, self.driver.find_element(*self.quantity))
        self.driver.find_element(*self.quantity).click()
        time.sleep(2)
        webdriver.ActionChains(self.driver).send_keys(Keys.DELETE).perform()
        time.sleep(2)
        self.driver.find_element(*self.quantity).send_keys("2")
        time.sleep(2)

    def recalculate_total_price_in_mini_basket(self):
        self.driver.find_element(*self.recalculate_quantity).click()
        time.sleep(4)

    def remove_product_from_mini_basket(self):
        self.driver.find_element(*self.remove_product).click()
        time.sleep(2)
        self.driver.find_element(*self.confirm_remove_product).click()
        time.sleep(2)
        webdriver.ActionChains(self.driver).move_to_element(self.driver.find_element(*self.basket_icon)).perform()
        time.sleep(2)

    def confirm_that_mini_basket_is_empty(self):
        return self.driver.find_element(*self.basket_icon).text

    def go_from_mini_basket_to_main_view_of_basket(self):
        self.driver.find_element(*self.view_and_edit_basket).click()
        WebDriverWait(self.driver, 15, 0.25).until(ec.url_changes)

    def get_number_of_products_in_mini_basket(self):
        return self.driver.find_element(*self.empty_basket_text).text

    def get_number_of_items_in_mini_basket(self):
        return self.driver.find_element(*self.number_of_items_in_basket).text