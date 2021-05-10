import unittest
from pages.base.default_setup import setup
from pages.signup_page_object import SignupPage


class TestSignup(unittest.TestCase):
    def setUp(self) -> None:
        setup(self)
        self.signup_page = SignupPage(self.driver)
        self.signup_page.open()

    def testNoEmail(self):
        self.signup_page.signup("", "", "", "")
        self.assertTrue(self.signup_page.login_component.check_email_error_message("Заполните поле"))

    def testNoUsername(self):
        self.signup_page.signup("", "", "", "")
        self.assertTrue(self.signup_page.login_component.check_username_error_message("Заполните поле"))

    def testNoPassword(self):
        self.signup_page.signup("", "", "", "")
        self.assertTrue(self.signup_page.login_component.check_password_error_message("Заполните поле"))

    def testNoRepeatedPassword(self):
        self.signup_page.signup("wrong@wrong.wrong", "wrongusername", "abcdefg", "abcdef")
        self.assertTrue(self.signup_page.login_component.check_password_error_message("Пароли не совпадают"))

    def testExistingEmail(self):
        self.signup_page.signup(self.EMAIL, "wrongusername", self.PASSWORD, self.PASSWORD)
        self.assertTrue(self.signup_page.login_component.check_errors_message("Email уже существует"))

    def testExistingUsername(self):
        self.signup_page.signup("wrong@wrong.wrong", self.LOGIN, self.PASSWORD, self.PASSWORD)
        self.assertTrue(self.signup_page.login_component.check_errors_message("Имя пользователя уже существует"))

    def testInvalidUsername(self):
        self.signup_page.signup(self.EMAIL, "abc#123?", self.PASSWORD, self.PASSWORD)
        self.assertTrue(self.signup_page.login_component.check_username_error_message("Имя может содержать только "
                                                                                      "буквы и цифры"))

    def testTooSmallPassword(self):
        password = "abc123"
        self.signup_page.signup("wrong@wrong.wrong", "wrongusername", password, password)
        self.assertTrue(self.signup_page.login_component.check_password_error_message("Длина пароля от 8 до 30 "
                                                                                      "символов\nМожет содержать "
                                                                                      "только латинские буквы и цифры"))

    def testTooBigPassword(self):
        password = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
        self.signup_page.signup("wrong@wrong.wrong", "wrongusername", password, password)
        self.assertTrue(self.signup_page.login_component.check_password_error_message("Длина пароля от 8 до 30 "
                                                                                      "символов\nМожет содержать "
                                                                                      "только латинские буквы и цифры"))

    def testInvalidPassword(self):
        password = "abcde12$3?4%f"
        self.signup_page.signup("wrong@wrong.wrong", "wrongusername", password, password)
        self.assertTrue(self.signup_page.login_component.check_password_error_message("Длина пароля от 8 до 30 "
                                                                                      "символов\nМожет содержать "
                                                                                      "только латинские буквы и цифры"))

    def tearDown(self) -> None:
        self.driver.quit()
