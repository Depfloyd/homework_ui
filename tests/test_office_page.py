import pytest


@pytest.mark.usefixtures('office_soft_page')
def test_add_to_cart_button(office_soft_page):
    office_soft_page.open_page()
    office_soft_page.click_add_to_cart_button()
    office_soft_page.check_cart_counter('1')


@pytest.mark.usefixtures('office_soft_page')
def test_plus_button(office_soft_page):
    office_soft_page.open_page()
    office_soft_page.click_plus_button()
    office_soft_page.check_quantity_counter('2')


@pytest.mark.usefixtures('office_soft_page')
def test_product_title(office_soft_page):
    office_soft_page.open_page()
    office_soft_page.check_product_title('Office Design Software')
