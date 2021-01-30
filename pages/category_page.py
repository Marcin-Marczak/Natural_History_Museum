from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class CategoryPages:

    def __init__(self, driver):
        self.driver = driver
        self.cookie = (By.ID, "js-gdpr-accept")
        self.filter_label = (By.XPATH, "//div[@class='filter-options-item']")
        self.filter_value = (By.XPATH, "//a[@href='https://www.nhmshop.co.uk/books.html?cat=1154']")
        self.filter_value_text = (By.XPATH, "//span[@class='filter-value']")
        self.product_name = (By.XPATH, "//a[@class='product-item-link']")
        self.add_to_basket_button = (By.XPATH, "//button[@title='Add to basket']")
        self.main_basket_link = (By.LINK_TEXT, "shopping basket")

    def go_to_main_basket_page(self):
        self.driver.find_element(*self.main_basket_link).click()
        WebDriverWait(self.driver, 15).until(ec.url_contains, "cart")

    def set_filter_label_and_value(self, url_category_page):
        self.driver.get(url_category_page)
        self.driver.find_element(*self.cookie).click()
        self.driver.find_element(*self.filter_label).click()
        self.driver.find_element(*self.filter_value).click()

    def get_text_of_category_set_in_filter(self):
        WebDriverWait(self.driver, 10, 0.25).until(ec.visibility_of_element_located, self.driver.find_element(*self.filter_value_text))
        return self.driver.find_element(*self.filter_value_text).text

    def get_first_product_name_from_list(self):
        return self.driver.find_element(*self.product_name).text

    def add_first_products_from_list_to_basket(self):
        self.driver.find_element(*self.add_to_basket_button).click()
        time.sleep(3)

    def go_to_page_of_first_product(self):
        self.driver.find_element(*self.product_name).click()