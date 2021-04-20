import urllib.parse as parser
from selenium import webdriver


class Page:
    BASE_URL = 'https://musicexpress.sarafa2n.ru/'
    PATH = ''
    driver: webdriver

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = parser.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()
