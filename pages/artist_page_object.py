from pages.base.default_component import Component
from pages.base.default_page_object import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ArtistPage(Page):
    PATH = '/album/9'

    def __init__(self, driver):
        super().__init__(driver)
        self.artist_component = ArtistComponent(self.driver)

    def get_artist_name(self):
        return self.artist_component.get_artist_name()


class ArtistComponent(Component):
    ARTIST_NAME = '//div[@class="artist-page-preview__title"]'

    def get_artist_name(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.visibility_of_element_located((By.XPATH, self.ARTIST_NAME))
        ).text
