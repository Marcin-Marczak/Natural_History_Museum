from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


class ReviewAndPaymentsPage:

    def __init__(self, driver):
        self.driver = driver
        self.product_name = (By.XPATH, "//strong[@class='product-item-name']")
        self.paypal_radio_button = (By.XPATH, "//input[@name='payment[method]']")
        self.continue_to_paypal_button = (By.XPATH, "//button[@class='action primary checkout']")

    def get_name_of_product_on_review_and_payments_page(self):
        return self.driver.find_element(*self.product_name).get_attribute("textContent")

    def choose_paypal_and_go_to_paypal_page(self):
        WebDriverWait(self.driver, 15).until(ec.element_to_be_clickable, self.driver.find_element(*self.paypal_radio_button))
        self.driver.find_element(*self.paypal_radio_button).click()
        self.driver.find_element(*self.continue_to_paypal_button).click()
        WebDriverWait(self.driver, 15).until(ec.url_changes)
        time.sleep(6)