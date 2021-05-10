import unittest
from pages.base.default_setup import setup
from pages.login_page_object import LoginPage
from pages.profile_page_object import ProfilePage


class TestSubscribes(unittest.TestCase):
    def setUp(self) -> None:
        setup(self)
        self.login_page = LoginPage(self.driver)
        self.login_page.auth(self.EMAIL, self.PASSWORD)
        self.profile1_page = ProfilePage(self.driver)
        self.profile2_page.PATH = '/profile/' + self.EMAIL
        self.profile1_page.open()
        self.profile2_page = ProfilePage(self.driver)
        self.profile2_page.PATH = '/profile/' + self.EMAIL2
        self.profile2_page.open()

    def testSubscribe(self):
        self.profile2_page.click_subscribe()
        self.driver.refresh()
        self.profile1_page.click_subscriptions()
        self.assertTrue(self.profile1_page.is_subscribed(self.EMAIL2))
        self.profile2_page.click_subscribers()
        self.assertTrue(self.profile1_page.is_subscription(self.USERNAME))

    def tearDown(self) -> None:
        self.driver.quit()
