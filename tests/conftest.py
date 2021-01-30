import pytest
from utils.driver_factory import DriverFactory
import random

browsers = ["chrome", "opera"]


@pytest.fixture()
def setup(request):
    driver = DriverFactory.get_driver(random.choice(browsers))
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


