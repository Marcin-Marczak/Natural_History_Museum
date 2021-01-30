from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import time


class PagesOpenedFromBookmarks:

    def __init__(self, driver):
        self.driver = driver
        self.results_sorter = (By.ID, "sorter")
        self.product_price = (By.XPATH, "//span[@data-price-type='finalPrice']")
        self.product_name = (By.XPATH, "//a[@class='product-item-link']")
        self.descending_order = (By.XPATH, "//a[@title='Set Descending Direction']")

    def sort_results_by_price_descending(self, price_results_sorter):
        WebDriverWait(self.driver, 15, 0.25).until(ec.element_to_be_clickable, self.driver.find_element(*self.results_sorter))
        self.driver.find_element(*self.results_sorter).click()
        self.driver.implicitly_wait(10)
        Select(self.driver.find_element(*self.results_sorter)).select_by_value(price_results_sorter)
        self.driver.find_element(*self.descending_order).click()
        time.sleep(3)

        prices = self.driver.find_elements(*self.product_price)
        products_prices = []
        for i in prices:
            i = i.text[1:]
            products_prices.append(i)

        products_prices_copy = products_prices[:]
        products_prices_copy.sort(reverse=True)

        if products_prices_copy == products_prices:
            return "passed"

    def sort_results_by_name_descending(self, name_results_sorter):
        WebDriverWait(self.driver, 15, 0.25).until(ec.element_to_be_clickable, self.driver.find_element(*self.results_sorter))
        self.driver.find_element(*self.results_sorter).click()
        self.driver.implicitly_wait(10)
        Select(self.driver.find_element(*self.results_sorter)).select_by_value(name_results_sorter)
        self.driver.find_element(*self.descending_order).click()
        time.sleep(3)

        names = self.driver.find_elements(*self.product_name)
        products_names = []

        for i in names:
            i = i.text
            products_names.append(i)

        products_names_copy = products_names[:]
        products_names_copy.sort(reverse=True)

        if products_names_copy == products_names:
            return "passed"