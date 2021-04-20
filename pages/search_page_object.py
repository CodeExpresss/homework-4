from pages.base.default_component import Component
from pages.base.default_page_object import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SearchPage(Page):
    PATH = '/search'

    def __init__(self, driver):
        super().__init__(driver)
        self.search_component = SearchComponent(self.driver)

    def exec_query(self, query):
        self.search_component.set_query_text(query)

    def get_incorrect_search_message(self):
        return self.search_component.get_incorrect_search_message()

    def get_void_search_message(self):
        return self.search_component.get_void_search_message()

    def get_query_results_albums(self):
        return self.search_component.get_query_results_albums()

    def get_query_results_users(self):
        return self.search_component.get_query_results_users()

    def get_query_results_songs(self):
        return self.search_component.get_query_results_songs()

    def click_user_result(self):
        self.search_component.click_user_result()


class SearchComponent(Component):
    QUERY_INPUT = '//input[@class="header__search-input"]'
    QUERY_MESSAGE = '//div[@class="search-page-placeholder__title"]'
    ALBUMS_RESULT = '//div[@class="wrapper_albums"]'
    USERS_RESULT = '//div[@class="wrapper_users"]'
    SONGS_RESULT = '//div[@class="track-item"]'
    USERS_RESULT_CLICKABLE = '//a[@class="user-item"]'

    INCORRECT_QUERY_MESSAGE = 'По вашему запросу ничего не найдено.'
    VOID_QUERY_MESSAGE = 'Давайте что-нибудь найдём!'

    def set_query_text(self, query: str):
        search_component = WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.QUERY_INPUT))
        )
        search_component.send_keys(query)

    def get_incorrect_search_message(self):
        WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.text_to_be_present_in_element((By.XPATH, self.QUERY_MESSAGE), self.INCORRECT_QUERY_MESSAGE)
        )

        return self.driver.find_element_by_xpath(self.QUERY_MESSAGE).text

    def get_void_search_message(self):
        WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.text_to_be_present_in_element((By.XPATH, self.QUERY_MESSAGE), self.VOID_QUERY_MESSAGE)
        )

        return self.driver.find_element_by_xpath(self.QUERY_MESSAGE).text

    def get_query_results_albums(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.ALBUMS_RESULT))
        ).text

    def get_query_results_users(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.USERS_RESULT))
        ).text

    def get_query_results_songs(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.SONGS_RESULT))
        ).text

    def click_user_result(self):
        WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.element_to_be_clickable((By.XPATH, self.USERS_RESULT_CLICKABLE))
        ).click()
