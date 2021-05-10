import unittest
from pages.base.default_setup import setup
from pages.login_page_object import LoginPage


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        setup(self)
        self.login_page = LoginPage(self.driver)
        self.login_page.open()

    def testWrongEmail(self):
        self.login_page.auth(self.EMAIL, "васяпупкин")
        self.assertTrue(self.login_page.login_component.check_error_message("Неверный логин или пароль"))

    def testWrongPassword(self):
        self.login_page.auth("wrong@email.wrong", self.PASSWORD)
        self.assertTrue(self.login_page.login_component.check_error_message("Неверный логин или пароль"))

    def testCorrectEmailAndPassword(self):
        self.login_page.auth(self.EMAIL, self.PASSWORD)
        self.assertTrue(self.login_page.login_component.check_error_message(""))

    def testCorrectLoginAndPassword(self):
        self.login_page.auth(self.LOGIN, self.PASSWORD)
        self.assertTrue(self.login_page.login_component.check_error_message(""))

    def tearDown(self) -> None:
        self.driver.quit()
