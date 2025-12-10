from pages.base_page import BasePage
from pages.locators import cart_locators


class CartPage(BasePage):
    page_url = '/shop/cart'

    def check_page_title(self, text: str):
        header_title = self.find(cart_locators.ORDER_OVERVIEW_TITLE)
        assert header_title.text == text

    def check_empty_cart_message(self, text: str):
        empty_cart_message = self.find(cart_locators.EMPTY_CART_MESSAGE)
        assert empty_cart_message.text == text

    def check_bread_crumbs(self, text: str):
        payment_bread_crumbs = self.find(cart_locators.PAYMENT_BREAD_CRUMBS)
        assert payment_bread_crumbs.text == text
