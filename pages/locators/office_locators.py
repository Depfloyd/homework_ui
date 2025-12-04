from selenium.webdriver.common.by import By


ADD_TO_CART_BUTTON = (By.XPATH, '//a[@id="add_to_cart"]')
CART_COUNT = (By.XPATH, 
           '(//sup[@class="my_cart_quantity badge text-bg-primary '
           'position-absolute top-0 end-0 mt-n1 me-n1 rounded-pill"]'
           '[normalize-space()="1"])[2]')
