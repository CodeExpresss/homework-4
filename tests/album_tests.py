import unittest
from pages.base.default_setup import setup
from pages.album_page_object import AlbumPage
from pages.artist_page_object import ArtistPage


class TestAlbum(unittest.TestCase):
    def setUp(self) -> None:
        setup(self)
        self.album_page = AlbumPage(self.driver)
        self.artist_page = ArtistPage(self.driver)
        self.album_page.open()

    def testAlbumAddToQueue(self):
        self.album_page.click_play_button()
        track_photo_url = self.album_page.get_track_photo_url()
        album_photo_url = self.album_page.get_album_photo_url()
        self.assertEqual(track_photo_url, album_photo_url)

    def testAlbumAddToQueueFirstTrack(self):
        self.album_page.click_play_button()
        current_track_name = self.album_page.get_current_track_name()
        first_album_track_name = self.album_page.get_first_track_name()
        self.assertEqual(current_track_name, first_album_track_name)

    def testAlbumArtistClickable(self):
        album_page_name = self.album_page.get_artist_name()
        self.album_page.click_artist_name()
        artist_page_name = self.artist_page.get_artist_name()
        self.assertEqual(album_page_name, artist_page_name)

    def tearDown(self) -> None:
        self.driver.quit()
