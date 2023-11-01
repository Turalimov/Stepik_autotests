import sys
sys.path.append('/tests/config')
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from config.data import Data
from config.links import Links


def test_names():
    for name in Data.names_list:
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        browser.get(Links.GOOGLE)
        search_bar = browser.find_element('xpath', "//textarea[@name='q']")
        search_bar.clear()
        search_bar.send_keys(name)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)
        browser.quit()
