import pytest
from pages.main_page import MainPage
from pages.category_page import CategoryPages
from pages.page_open_from_bookmark import PagesOpenedFromBookmarks
from pages.mini_basket_page import MiniBasketPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.shipping_page import ShippingPage
from pages.review_and_payments_page import ReviewAndPaymentsPage
from tests.data_used_in_tests import *


@pytest.mark.usefixtures("setup")
class TestShopOnline:

    def test_01_open_main_shop_page(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page(url_main_page)
        assert self.driver.current_url == url_main_page

    def test_02_open_category_page_from_bookmark(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page(url_main_page)
        main_page.go_to_category_page()
        assert self.driver.current_url == url_category_page

    def test_03_set_filter(self):
        category_page = CategoryPages(self.driver)
        category_page.set_filter_label_and_value(url_category_page)
        assert category_value == category_page.get_text_of_category_set_in_filter()

    def test_04_sort_products_by_price_descending(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page(url_main_page)
        main_page.go_to_page_1_from_bookmark()
        assert url_page_from_bookmark in self.driver.current_url
        page_opened_from_bookmark = PagesOpenedFromBookmarks(self.driver)
        assert page_opened_from_bookmark.sort_results_by_price_descending(price_results_sorter) == "passed"

    def test_05_sort_products_by_name_descending(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page(url_main_page)
        main_page.go_to_page_1_from_bookmark()
        assert url_page_from_bookmark in self.driver.current_url
        page_opened_from_bookmark = PagesOpenedFromBookmarks(self.driver)
        assert page_opened_from_bookmark.sort_results_by_name_descending(name_results_sorter) == "passed"

    def test_06_add_product_to_basket_and_change_quantity_and_remove_in_mini_basket(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page(url_main_page)
        main_page.go_to_category_page()
        category_page = CategoryPages(self.driver)
        category_page.add_first_products_from_list_to_basket()
        mini_basket = MiniBasketPage(self.driver)
        mini_basket.open_mini_basket()
        mini_basket.change_quantity_in_mini_basket()
        mini_basket.recalculate_total_price_in_mini_basket()
        assert mini_basket.get_number_of_items_in_mini_basket() == "2"
        mini_basket.remove_product_from_mini_basket()
        assert mini_basket.confirm_that_mini_basket_is_empty() == empty_mini_basket_confirmation

    def test_07_add_product_to_basket_and_remove(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page(url_main_page)
        main_page.go_to_page_1_from_bookmark()
        category_page = CategoryPages(self.driver)
        product_name = category_page.get_first_product_name_from_list()
        category_page.add_first_products_from_list_to_basket()
        mini_basket = MiniBasketPage(self.driver)
        mini_basket.open_mini_basket()
        mini_basket.go_from_mini_basket_to_main_view_of_basket()
        basket_page = BasketPage(self.driver)
        assert basket_page.get_current_number_of_products_in_basket() == 1
        assert product_name in basket_page.get_name_of_only_one_product_in_basket()
        basket_page.remove_product_from_basket()
        mini_basket.open_mini_basket()
        assert mini_basket.get_number_of_products_in_mini_basket() == empty_mini_basket_confirmation

    def test_08_add_2_products_and_update_quantities_in_two_ways_in_basket(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page(url_main_page)
        main_page.go_to_page_2_from_bookmark()
        category_page = CategoryPages(self.driver)
        product_1_name = category_page.get_first_product_name_from_list()
        category_page.add_first_products_from_list_to_basket()
        main_page.go_to_page_3_from_bookmark()
        product_2_name = category_page.get_first_product_name_from_list()
        category_page.add_first_products_from_list_to_basket()
        mini_basket = MiniBasketPage(self.driver)
        mini_basket.open_mini_basket()
        mini_basket.go_from_mini_basket_to_main_view_of_basket()
        basket_page = BasketPage(self.driver)
        basket_page.get_current_number_of_products_in_basket()
        assert basket_page.get_current_number_of_products_in_basket() == 2
        basket_page.change_product_quantity_in_basket_using_quantity_field()
        basket_page.go_to_product_page_from_basket()
        product_page = ProductPage(self.driver)
        product_page.change_product_quantity_on_product_page()
        assert mini_basket.get_number_of_items_in_mini_basket() == "4"
        assert product_1_name in basket_page.get_name_of_first_product_in_basket()
        assert product_2_name in basket_page.get_name_of_second_product_in_basket()

    def test_09_entire_flow_from_open_shop_page_to_payment_page(self):
        main_page = MainPage(self.driver)
        main_page.open_main_page(url_main_page)
        main_page.go_to_category_page()
        category_page = CategoryPages(self.driver)
        category_page.go_to_page_of_first_product()
        product_page = ProductPage(self.driver)
        product_name = product_page.get_name_of_product_on_product_page()
        product_page.add_product_to_basket_on_product_page_and_go_to_basket()
        basket_page = BasketPage(self.driver)
        basket_page.go_to_checkout_page_from_basket()
        shipping_page = ShippingPage(self.driver)
        shipping_page.enter_email(email)
        shipping_page.enter_first_name(first_name)
        shipping_page.enter_last_name(last_name)
        shipping_page.enter_street_address(street_address)
        shipping_page.enter_city(city)
        shipping_page.enter_postal_code(postal_code)
        shipping_page.select_country(country_value)
        shipping_page.enter_phone_number(phone_number)
        shipping_page.go_to_review_and_payments_page()
        review_and_payments_page = ReviewAndPaymentsPage(self.driver)
        assert product_name in review_and_payments_page.get_name_of_product_on_review_and_payments_page()
        review_and_payments_page.choose_paypal_and_go_to_paypal_page()
        assert "paypal" in self.driver.current_url