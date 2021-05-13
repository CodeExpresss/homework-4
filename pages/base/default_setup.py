from selenium import webdriver
import os


def setup(test):
    test.EMAIL = os.environ['EMAIL']
    test.LOGIN = os.environ['LOGIN']
    test.PASSWORD = os.environ['PASSWORD']
    test.LOGIN2 = os.environ['LOGIN2']
    test.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
