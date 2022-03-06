from selenium import webdriver
import pytest

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

baseUrl = "https://www.flipkart.com/"
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)\

driver.get(baseUrl)
driver.quit()