from selenium.webdriver.common.by import By


CUSTOMIZABLE_DESK_TITLE = (
    By.XPATH, '//a[@class="text-primary text-decoration-none" and contains(text(), "Customizable Desk")]'
    )
CUSTOMIZABLE_DESK_PRICE = (By.XPATH, '//span[@class="oe_currency_value" and contains(text(), "750.00")]')
SEARCH_FIELD = (By.XPATH, '(//input[@type="search" and @name="search" and @placeholder="Search..."])[2]')
CUSTOMIZABLE_DESK_SEARCH_RESULT = (By.XPATH, '//div[@class="o_search_result_item_detail px-3"]')
