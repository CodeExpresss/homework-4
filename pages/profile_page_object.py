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

    def click_subscribers(self):
        return self.profile_component.click_subscribers()

    def click_subscriptions(self):
        return self.profile_component.click_subscriptions()

    def is_subscribed(self, username):
        return self.profile_component.is_subscribed_or_subscription(username)

    def is_subscription(self, username):
        return self.profile_component.is_subscribed_or_subscription(username)


class ProfileComponent(Component):
    PROFILE_NAME = '//div[@class="profile-page__header-username"]'
    BUTTON_SUBSCRIBE = '//div[@class="profile-page__follow button-primary"]'
    BUTTON_SUBSCRIBERS = '//div[@class="profile-page__toggle-item", @data-class="profile-page__item_subscribers"]'
    BUTTON_SUBSCRIPTIONS = '//div[@class="profile-page__toggle-item", @data-class="profile-page__item_subscriptions"]'
    # DIV_SUBSCRIPTIONS = '//div[@class="profile-page__item profile-page__item_subscriptions profile-page__item_active"]'
    USER_LINK1 = '//a[@class="user-item", @href="/profile/'
    USER_LINK2 = '"]'

    def get_user_name(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.visibility_of_element_located((By.XPATH, self.PROFILE_NAME))
        ).text

    def click_subscribe(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.BUTTON_SUBSCRIBE))
        ).click()

    def click_subscribers(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.BUTTON_SUBSCRIBERS))
        ).click()

    def click_subscriptions(self):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.BUTTON_SUBSCRIPTIONS))
        ).click()

    def is_subscribed_or_subscription(self, username):
        return WebDriverWait(self.driver, self.TIMEOUT, self.UPDATE).until(
            EC.presence_of_element_located((By.XPATH, self.USER_LINK1 + username + self.USER_LINK2))
        )
