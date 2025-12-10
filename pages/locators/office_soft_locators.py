from selenium.webdriver.common.by import By


ADD_TO_CART_BUTTON = (By.XPATH, '//a[@id="add_to_cart"]')
CART_COUNTER = (By.XPATH, 
            '//sup[@class="my_cart_quantity badge text-bg-primary '
            'position-absolute top-0 end-0 mt-n1 me-n1 rounded-pill"]'
            '[normalize-space()="1"]'
            )
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h1')
PLUS_BUTTON = (By.CSS_SELECTOR, 'i.fa.fa-plus')
QUANTITY_COUNTER = (By.CSS_SELECTOR, 'input.form-control.quantity')
