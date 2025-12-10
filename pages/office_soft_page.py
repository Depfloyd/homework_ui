from pages.base_page import BasePage
from pages.locators import office_soft_locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OfficeSoftPage(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    def click_add_to_cart_button(self):
        add_to_cart_button = self.find(office_soft_locators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def check_cart_counter(self, text: str):
        wait = WebDriverWait(self.driver, 15)
        cart_counter = wait.until(EC.visibility_of_element_located(office_soft_locators.CART_COUNTER))
        assert cart_counter.text == text

    def click_plus_button(self):
        plus_button = self.find(office_soft_locators.PLUS_BUTTON)
        plus_button.click()

    def check_quantity_counter(self, text: str):
        wait = WebDriverWait(self.driver, 15)
        wait.until(
            lambda driver: self.find(office_soft_locators.QUANTITY_COUNTER).get_attribute('value') == text
        )
        quantity_counter = self.find(office_soft_locators.QUANTITY_COUNTER)
        assert quantity_counter.get_attribute('value') == text

    def check_product_title(self, text: str):
        product_title = self.find(office_soft_locators.PRODUCT_TITLE)
        assert product_title.text == text
