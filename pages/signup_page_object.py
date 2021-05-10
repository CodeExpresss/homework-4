from pages.base.default_component import Component
from pages.base.default_page_object import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SignupPage(Page):
    PATH = '/signup/'

    def __init__(self, driver):
        super().__init__(driver)
        self.login_component = SignupComponent(self.driver)

    def signup(self, email, username, password, repeated_password):
        self.login_component.set_email_field(email)
        self.login_component.set_username_field(username)
        self.login_component.set_password1_field(password)
        self.login_component.set_password2_field(repeated_password)
        self.login_component.submit()


class SignupComponent(Component):
    EMAIL_FIELD = '//input[@name="email"]'
    USERNAME_FIELD = '//input[@name="username"]'
    PASSWORD1_FIELD = '//input[@name="password1"]'
    PASSWORD2_FIELD = '//input[@name="password2"]'
    SUBMIT = '//input[@class="form-signup__submit button-primary"]'
    ERRORS_FIELD = '//div[@class="signup-page__errors"]'
    EMAIL_ERROR_FIELD = '//div[contains(@class, "email-error")]'
    USERNAME_ERROR_FIELD = '//div[contains(@class, "username-error")]'
    PASSWORD_ERROR_FIELD = '//div[contains(@class, "password-error")]'

    def set_email_field(self, email):
        element = WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.EMAIL_FIELD))
        )
        element.send_keys(email)

    def set_username_field(self, username):
        element = WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.USERNAME_FIELD))
        )
        element.send_keys(username)

    def set_password1_field(self, password):
        element = WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.PASSWORD1_FIELD))
        )
        element.send_keys(password)

    def set_password2_field(self, password):
        element = WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.PASSWORD2_FIELD))
        )
        element.send_keys(password)

    def submit(self):
        WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.element_to_be_clickable((By.XPATH, self.SUBMIT))
        ).click()

    def check_errors_message(self, expected_errors_message):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.text_to_be_present_in_element((By.XPATH, self.ERRORS_FIELD), expected_errors_message)
        )

    def check_email_error_message(self, expected_error_message):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.text_to_be_present_in_element((By.XPATH, self.EMAIL_ERROR_FIELD), expected_error_message)
        )

    def check_username_error_message(self, expected_error_message):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.text_to_be_present_in_element((By.XPATH, self.USERNAME_ERROR_FIELD), expected_error_message)
        )

    def check_password_error_message(self, expected_error_message):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.text_to_be_present_in_element((By.XPATH, self.PASSWORD_ERROR_FIELD), expected_error_message)
        )
