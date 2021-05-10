from pages.base.default_component import Component
from pages.base.default_page_object import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(Page):
    PATH = '/login/'

    def __init__(self, driver):
        super().__init__(driver)
        self.login_component = LoginComponent(self.driver)

    def auth(self, email, password):
        self.login_component.set_email_field(email)
        self.login_component.set_password_field(password)
        self.login_component.submit()


class LoginComponent(Component):
    EMAIL_FIELD = '//input[@name="login"]'
    PASSWORD_FIELD = '//input[@name="password"]'
    SUBMIT = '//input[@class="form-login__submit button-primary"]'
    ERRORS_FIELD = '//div[@class="login-page__errors"]'

    def set_email_field(self, email):
        element = WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.EMAIL_FIELD))
        )
        element.send_keys(email)

    def set_password_field(self, password):
        element = WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.PASSWORD_FIELD))
        )
        element.send_keys(password)

    def submit(self):
        WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.element_to_be_clickable((By.XPATH, self.SUBMIT))
        ).click()

    def check_error_message(self, expected_error_message):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.text_to_be_present_in_element((By.XPATH, self.ERRORS_FIELD), expected_error_message)
        )
