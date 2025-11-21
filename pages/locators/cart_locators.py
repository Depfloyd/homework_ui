from selenium.webdriver.common.by import By


ORDER_OVERVIEW_TITLE = (By.CSS_SELECTOR, 'h3.mb-4')
EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, 'div.js_cart_lines.alert.alert-info')
PAYMENT_BREAD_CRUMBS = (
    By.XPATH, '//p[contains(@class, "o_wizard_steplabel") and normalize-space()="Payment"]'
    )
