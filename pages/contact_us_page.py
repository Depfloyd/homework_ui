from pages.base_page import BasePage
from pages.locators import contact_us_locators as locators


class ContactUsPage(BasePage):
    page_url = '/contactus'

    def contact_us_form_send(self, name, phone, email, company, subject, question):