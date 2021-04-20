import unittest
from pages.base.default_setup import setup
from pages.search_page_object import SearchPage
from pages.profile_page_object import ProfilePage


class TestSearch(unittest.TestCase):
    def setUp(self) -> None:
        setup(self)
        self.search_page = SearchPage(self.driver)
        self.profile_page = ProfilePage(self.driver)
        self.search_page.open()

    def testVoidSearch(self):
        message = self.search_page.get_void_search_message()
        self.assertEqual(message, self.search_page.search_component.VOID_QUERY_MESSAGE)

    def testIncorrectQuery(self):
        query = "#$@$#@!$#!$!#!$@Y*&!@#HIU!@"
        self.search_page.exec_query(query)
        message = self.search_page.get_incorrect_search_message()
        self.assertEqual(message, self.search_page.search_component.INCORRECT_QUERY_MESSAGE)

    def testArtistSearch(self):
        query = "Eminem"
        self.search_page.exec_query(query)
        result_text = self.search_page.get_query_results_albums()
        self.assertEqual(result_text, query)

    def testUserSearch(self):
        self.search_page.exec_query(self.LOGIN)
        result_text = self.search_page.get_query_results_users()
        self.assertEqual(result_text, self.LOGIN)

    def testSongSearch(self):
        query = 'You Acting Like You Dont Know'
        self.search_page.exec_query(query)
        result_text = self.search_page.get_query_results_songs()
        self.assertTrue(query in result_text)

    def testUserSearchClickable(self):
        search_user_name = self.search_page.exec_query(self.LOGIN)
        self.search_page.click_user_result()
        profile_user_name = self.profile_page.get_user_name()
        self.assertEqual(search_user_name, profile_user_name)

    def tearDown(self) -> None:
        self.driver.quit()
