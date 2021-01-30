from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.bookmark_1_displayed_on_main_page = (By.LINK_TEXT, "Books")
        self.bookmark_2_displayed_on_main_page = (By.LINK_TEXT, "Home")
        self.bookmark_3_displayed_on_main_page = (By.LINK_TEXT, "Kids")
        self.bookmark_4_displayed_on_main_page = (By.LINK_TEXT, "Fashion")
        self.page_1_opened_from_bookmark = (By.LINK_TEXT, "Home accessories")
        self.page_2_opened_from_bookmark = (By.LINK_TEXT, "Soft toys")
        self.page_3_opened_from_bookmark = (By.LINK_TEXT, "Scarves")
        self.cookie = (By.ID, "js-gdpr-accept")

    def open_main_page(self, url_main_page):
        self.driver.get(url_main_page)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable, self.driver.find_element(*self.cookie))
        self.driver.find_element(*self.cookie).click()

    def go_to_category_page(self):
        self.driver.find_element(*self.bookmark_1_displayed_on_main_page).click()
        WebDriverWait(self.driver, 10, 0.25).until(ec.url_changes)

    def go_to_page_1_from_bookmark(self):
        webdriver.ActionChains(self.driver).move_to_element(self.driver.find_element(*self.bookmark_2_displayed_on_main_page)).perform()
        WebDriverWait(self.driver, 10, 0.25).until(ec.element_to_be_clickable, self.driver.find_element(*self.page_1_opened_from_bookmark))
        self.driver.find_element(*self.page_1_opened_from_bookmark).click()
        WebDriverWait(self.driver, 10, 0.25).until(ec.url_changes)

    def go_to_page_2_from_bookmark(self):
        webdriver.ActionChains(self.driver).move_to_element(self.driver.find_element(*self.bookmark_3_displayed_on_main_page)).perform()
        WebDriverWait(self.driver, 10, 0.25).until(ec.element_to_be_clickable, self.driver.find_element(*self.page_2_opened_from_bookmark))
        self.driver.find_element(*self.page_2_opened_from_bookmark).click()
        WebDriverWait(self.driver, 10, 0.25).until(ec.url_changes)

    def go_to_page_3_from_bookmark(self):
        webdriver.ActionChains(self.driver).move_to_element(self.driver.find_element(*self.bookmark_4_displayed_on_main_page)).perform()
        WebDriverWait(self.driver, 10, 0.25).until(ec.element_to_be_clickable, self.driver.find_element(*self.page_3_opened_from_bookmark))
        self.driver.find_element(*self.page_3_opened_from_bookmark).click()
        WebDriverWait(self.driver, 10, 0.25).until(ec.url_changes)