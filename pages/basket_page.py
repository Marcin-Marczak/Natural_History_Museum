from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
import time


class BasketPage:

    def __init__(self, driver):
        self.driver = driver
        self.edit_product = (By.XPATH, "//a[@class='action action-edit']")
        self.quantity = (By.XPATH, "//input[@class='input-text qty']")
        self.update_basket = (By.XPATH, "//button[@class='action update']")
        self.remove_product = (By.XPATH, "//a[@class='action action-delete']")
        self.product_name_in_basket = (By.XPATH, "//strong[@class='product-item-name']/a")
        self.proceed_to_checkout = (By.XPATH, "//button[@class='action primary checkout']")

    def get_current_number_of_products_in_basket(self):
        return len(self.driver.find_elements(*self.edit_product))

    def change_product_quantity_in_basket_using_quantity_field(self):
        self.driver.find_element(*self.quantity).click()
        time.sleep(3)
        webdriver.ActionChains(self.driver).send_keys(Keys.DELETE).perform()
        time.sleep(3)
        self.driver.find_element(*self.quantity).send_keys("2")
        time.sleep(3)
        update_button = self.driver.find_element(*self.update_basket)
        webdriver.ActionChains(self.driver).move_to_element(update_button).click(update_button).perform()
        time.sleep(4)

    def go_to_product_page_from_basket(self):
        self.driver.find_elements(*self.edit_product)[1].click()
        WebDriverWait(self.driver, 10, 0.25).until(ec.url_changes)

    def remove_product_from_basket(self):
        self.driver.find_element(*self.remove_product).click()
        time.sleep(4)

    def get_name_of_only_one_product_in_basket(self):
        return self.driver.find_element(*self.product_name_in_basket).get_attribute("textContent")

    def get_name_of_first_product_in_basket(self):
        return self.driver.find_elements(*self.product_name_in_basket)[2].get_attribute("textContent")

    def get_name_of_second_product_in_basket(self):
        return self.driver.find_elements(*self.product_name_in_basket)[3].get_attribute("textContent")

    def go_to_checkout_page_from_basket(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable, self.driver.find_element(*self.proceed_to_checkout))
        self.driver.find_element(*self.proceed_to_checkout).click()
        WebDriverWait(self.driver, 15).until(ec.url_contains, "shipping")