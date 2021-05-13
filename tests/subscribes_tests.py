import unittest
from pages.base.default_setup import setup
from pages.login_page_object import LoginPage
from pages.profile_page_object import ProfilePage


class TestSubscribes(unittest.TestCase):
    def setUp(self) -> None:
        setup(self)
        self.login_page = LoginPage(self.driver)
        self.login_page.open()
        self.login_page.auth(self.EMAIL, self.PASSWORD)
        self.profile_page = ProfilePage(self.driver)
        self.profile_page.PATH = '/profile/' + self.LOGIN2
        self.profile_page.open()

    def testSubscribe(self):
        self.profile_page.click_subscribe()
        self.assertTrue(self.profile_page.is_subscribed())

    def testUnsubscribe(self):
        self.profile_page.click_unsubscribe()
        self.assertTrue(self.profile_page.is_unsubscribed())

    def tearDown(self) -> None:
        self.driver.quit()
