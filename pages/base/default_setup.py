from selenium import webdriver
import os


def setup(test):
    test.EMAIL = os.environ['EMAIL']
    test.LOGIN = os.environ['LOGIN']
    test.PASSWORD = os.environ['PASSWORD']
    test.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
