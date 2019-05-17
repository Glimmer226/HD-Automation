# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Libs.get_selector import GetSelector
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from time import sleep


class Login:
    def __init__(self, driver):
        self.driver = driver

    def login(self, url="https://www.harley-davidson.com/us/en/index.html"):
        driver = self.driver
        # driver.maximize_window()
        driver.get(url)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.harley-davidson.com/us/en/index.html")
    g = GetSelector("C:\\Users\\glimmer.zhang\\Documents\\Python\\HD Automation\\config\\home_page.json")
    v = g.get_selector()

    a = driver.find_element_by_css_selector(v["Video"])
    print(a.get_attribute('autoplay'))
    assert a.get_attribute('autoplay') == 'true'


