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

    def click_subscribe(self):
        return self.profile_component.click_subscribe()

    def click_unsubscribe(self):
        return self.profile_component.click_unsubscribe()

    def is_subscribed(self):
        return self.profile_component.is_subscribed()

    def is_unsubscribed(self):
        return self.profile_component.is_unsubscribed()


class ProfileComponent(Component):
    PROFILE_NAME = '//div[@class="profile-page__header-username"]'
    BUTTON_SUBSCRIBE = '//div[@class="profile-page__follow button-primary"]'

    def get_user_name(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.visibility_of_element_located((By.XPATH, self.PROFILE_NAME))
        ).text

    def click_subscribe(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.BUTTON_SUBSCRIBE))
        ).click()

    def click_unsubscribe(self):
        return self.click_subscribe()

    def is_subscribed(self):
        WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.BUTTON_SUBSCRIBE))
        )
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.text_to_be_present_in_element((By.XPATH, self.BUTTON_SUBSCRIBE), 'Отписаться')
        )

    def is_unsubscribed(self):
        WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.BUTTON_SUBSCRIBE))
        )
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.text_to_be_present_in_element((By.XPATH, self.BUTTON_SUBSCRIBE), 'Подписаться')
        )
