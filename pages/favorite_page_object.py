from pages.base.default_component import Component
from pages.base.default_page_object import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class FavoritePage(Page):
    PATH = '/'

    def __init__(self, driver):
        super().__init__(driver)
        self.favorite_component = FavoriteComponent(self.driver)

    def get_track_add_button_element(self):
        return self.favorite_component.get_track_add_button_element()

    def get_favorite_link_item(self):
        return self.favorite_component.get_favorite_link_item()


class FavoriteComponent(Component):
    ADD_BUTTON = '//div[@class="track-item__icon add-favorite fas fa-plus"]'
    FAVORITE_LINK = '//a[@class="group-links__link"]'

    def get_track_add_button_element(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until_not(
            EC.presence_of_element_located((By.XPATH, self.ADD_BUTTON))
        )

    def get_favorite_link_item(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until_not(
            EC.presence_of_element_located((By.XPATH, self.FAVORITE_LINK))
        )

