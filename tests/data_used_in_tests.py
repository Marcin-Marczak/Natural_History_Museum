import random
from faker import Faker
fake = Faker("en_GB")
letters = (65, 90)

url_main_page = "https://www.nhmshop.co.uk/"
url_category_page = "https://www.nhmshop.co.uk/books.html"
category_value = "Biographies"
url_page_from_bookmark = "for-the-home/homeware"
price_results_sorter = "price"
name_results_sorter = "name"
empty_mini_basket_confirmation = "You have no items in your shopping basket."
email = fake.email()
first_name = fake.first_name_male()
last_name = fake.last_name_male()
street_address = fake.street_address()
city = "Bristol"
postal_code = "BS" + str(random.randint(1, 91)) + " " + str(random.randint(1, 9)) + chr(random.choice(letters)) + chr(random.choice(letters))
country_value = "GB"
phone_number = fake.phone_number()