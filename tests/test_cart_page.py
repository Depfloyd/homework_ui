import pytest


@pytest.mark.usefixtures('cart_page')
def test_page_title(cart_page):
    cart_page.open_page()
    cart_page.check_page_title('Order overview')


@pytest.mark.usefixtures('cart_page')
def test_empty_cart_message(cart_page):
    cart_page.open_page()
    cart_page.check_empty_cart_message('Your cart is empty!')


@pytest.mark.usefixtures('cart_page')
def test_payment_bread_crumbs(cart_page):
    cart_page.open_page()
    cart_page.check_payment_bread_crumbs('Payment')
