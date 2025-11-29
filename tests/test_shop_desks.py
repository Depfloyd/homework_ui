import pytest


@pytest.mark.usefixtures('desks_page')
def test_customizable_desk_title(desks_page):
    desks_page.open_page()
    desks_page.check_customizable_desk_title('Customizable Desk')


@pytest.mark.usefixtures('desks_page')
def test_customizable_desk_price(desks_page):
    desks_page.open_page()
    desks_page.check_customizable_desk_price('750.00')


@pytest.mark.usefixtures('desks_page')
def test_search_customizable_desk(desks_page):
    desks_page.open_page()
    desks_page.search_customizable_desk('Customizable Desk')
