from pages.base.default_component import Component
from pages.base.default_page_object import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AlbumPage(Page):
    PATH = '/album/9'

    def __init__(self, driver):
        super().__init__(driver)
        self.album_component = AlbumComponent(self.driver)

    def click_play_button(self):
        self.album_component.click_play_button()

    def get_track_photo_url(self):
        return self.album_component.get_track_photo_url()

    def get_album_photo_url(self):
        return self.album_component.get_album_photo_url()

    def get_first_track_name(self):
        return self.album_component.get_first_track_name()

    def get_current_track_name(self):
        return self.album_component.get_current_track_name()

    def get_artist_name(self):
        return self.album_component.get_artist_name()

    def click_artist_name(self):
        return self.album_component.click_artist_name()


class AlbumComponent(Component):
    PLAY_BUTTON = '//div[@class="button-primary button-play-album"]'
    TRACK_PHOTO = '//img[@class="player-track__album"]'
    ALBUM_PHOTO = '//img[@class="header-item__poster"]'
    ALBUM_TRACK = '//div[@class="track-item__title"]'
    CURRENT_TRACK = '//div[@class="player-track__title"]'
    ARTIST_NAME = '//a[@class="header-item__group"]'

    def click_play_button(self):
        WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.PLAY_BUTTON))
        ).click()

    def get_track_photo_url(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.TRACK_PHOTO))
        ).get_attribute("src")

    def get_album_photo_url(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.ALBUM_PHOTO))
        ).get_attribute("src")

    def get_first_track_name(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.ALBUM_TRACK))
        ).text

    def get_current_track_name(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.CURRENT_TRACK))
        ).text

    def get_artist_name(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.ARTIST_NAME))
        ).text

    def click_artist_name(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.ARTIST_NAME))
        ).click()
