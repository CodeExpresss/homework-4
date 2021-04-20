import unittest
from pages.base.default_setup import setup
from pages.favorite_page_object import FavoritePage
from pages.login_page_object import LoginPage


class TestFavorite(unittest.TestCase):
    def setUp(self) -> None:
        setup(self)
        self.favorite_page = FavoritePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.favorite_page.open()

    def testAddToFavoriteButtonInvisible(self):
        result = self.favorite_page.get_track_add_button_element()
        self.assertTrue(result)

    def testFavoriteLinkInvisible(self):
        result = self.favorite_page.get_favorite_link_item()
        self.assertTrue(result)

    def tearDown(self) -> None:
        self.driver.quit()
