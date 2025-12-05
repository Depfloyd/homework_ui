from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from pages.cart_page import CartPage
from pages.desks_page import DesksPage
from pages.office_soft_page import OfficeSoftPage
from time import sleep


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()
    # sleep(3)
    yield chrome_driver
    chrome_driver.quit()



@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture()
def desks_page(driver):
    return DesksPage(driver)


@pytest.fixture()
def office_soft_page(driver):
    return OfficeSoftPage(driver)