from pages.base_page import BasePage
from pages.locators import shop_locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DesksPage(BasePage):
    page_url = '/shop/category/desks-1'

    def check_customizable_desk_title(self, text: str):
        customizable_desk_title = self.find(shop_locators.CUSTOMIZABLE_DESK_TITLE)
        assert customizable_desk_title.text == text

    def check_customizable_desk_price(self, text: str):
        customizable_desk_price = self.find(shop_locators.CUSTOMIZABLE_DESK_PRICE)
        assert customizable_desk_price.text == text
    
    def search_customizable_desk(self, text: str):
        wait = WebDriverWait(self.driver, 15)
        search_field = wait.until(EC.visibility_of_element_located(shop_locators.SEARCH_FIELD))
        search_button = wait.until(EC.visibility_of_element_located(shop_locators.SEARCH_BUTTON))
        search_field.click()
        search_field.send_keys(text)
        search_button.click()
        customizable_desk_search_result = wait.until(
            EC.visibility_of_element_located(shop_locators.CUSTOMIZABLE_DESK_SEARCH_RESULT)
            )
        assert customizable_desk_search_result.text == text