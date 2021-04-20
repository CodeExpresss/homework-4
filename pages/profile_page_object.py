from pages.base.default_component import Component
from pages.base.default_page_object import Page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(Page):
    PATH = '/album/9'

    def __init__(self, driver):
        super().__init__(driver)
        self.profile_component = ProfileComponent(self.driver)

    def get_user_name(self):
        return self.profile_component.get_user_name()


class ProfileComponent(Component):
    PROFILE_NAME = '//div[@class="profile-page__header-username"]'

    def get_user_name(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.visibility_of_element_located((By.XPATH, self.PROFILE_NAME))
        ).text
