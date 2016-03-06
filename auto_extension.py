from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import wine

secret_keys = wine.keys("./secret.json")

while True:
    driver = webdriver.Firefox()
    wine.access_listpage(secret_keys, driver)
    wine.send_extension(driver)
    driver.close()
    time.sleep(250000)
