from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time


def keys(filename):
    with open(filename) as f:
        secret_keys = json.load(f)
    return secret_keys


def access_listpage(secret_keys, driver):
    driver.get("https://wine.wul.waseda.ac.jp/patroninfo*jpn")
    time.sleep(2)

    elem = driver.find_element_by_name("extpatid")
    elem.send_keys(secret_keys["user"])
    
    elem2 = driver.find_element_by_name("extpatpw")
    elem2.send_keys(secret_keys["pw"])
    
    submit = driver.find_element_by_link_text("送信")
    submit.click()
    time.sleep(2)

    list_all = driver.find_element_by_partial_link_text("貸出中です")
    list_all.click()
    time.sleep(2)


def send_extension(driver):
    """
    前提：借りている書籍のリストにいること
    """
    
    driver.find_element_by_name("requestRenewAll").click()
    time.sleep(2)
    
    driver.find_element_by_name("renewall").click()
    time.sleep(2)
