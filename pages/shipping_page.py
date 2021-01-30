from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import time


class ShippingPage:

    def __init__(self, driver):
        self.driver = driver
        self.email = (By.XPATH, "//fieldset[@id='customer-email-fieldset']/div/div/input")
        self.first_name = (By.XPATH, "//input[@name='firstname']")
        self.last_name = (By.XPATH, "//input[@name='lastname']")
        self.street_address = (By.XPATH, "//input[@name='street[0]']")
        self.city = (By.XPATH, "//input[@name='city']")
        self.postal_code = (By.XPATH, "//input[@name='postcode']")
        self.country = (By.XPATH, "//select[@name='country_id']")
        self.phone_number = (By.XPATH, "//input[@name='telephone']")
        self.next_button = (By.XPATH, "//button[@class='button action continue primary']")

    def enter_email(self, email):
        self.driver.find_element(*self.email).click()
        time.sleep(2)
        self.driver.find_element(*self.email).send_keys(email)

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name).click()
        time.sleep(2)
        self.driver.find_element(*self.first_name).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name).click()
        time.sleep(2)
        self.driver.find_element(*self.last_name).send_keys(last_name)

    def enter_street_address(self, street_address):
        self.driver.find_element(*self.street_address).click()
        time.sleep(2)
        self.driver.find_element(*self.street_address).send_keys(street_address)

    def enter_city(self, city):
        self.driver.find_element(*self.city).click()
        time.sleep(2)
        self.driver.find_element(*self.city).send_keys(city)

    def enter_postal_code(self, postal_code):
        self.driver.find_element(*self.postal_code).click()
        time.sleep(2)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)

    def select_country(self, country_value):
        self.driver.find_element(*self.country).click()
        self.driver.implicitly_wait(10)
        Select(self.driver.find_element(*self.country)).select_by_value(country_value)
        time.sleep(2)

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number).click()
        time.sleep(2)
        self.driver.find_element(*self.phone_number).send_keys(phone_number)

    def go_to_review_and_payments_page(self):
        self.driver.find_element(*self.next_button).click()
        WebDriverWait(self.driver, 15).until(ec.url_contains, "payment")