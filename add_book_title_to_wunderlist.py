from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import wine
import wunderpy
from requests_oauthlib import OAuth2Session


secret_keys = wine.keys("./secret.json")

driver = webdriver.Firefox()
wine.access_listpage(secret_keys, driver)
titles = wine.get_book_titles_from_list(driver)
dates = wine.get_book_due_from_list(driver)
driver.close()

wunderlist = wunderpy.connect_wunderlist("./secret.json")

id_list = wunderpy.show_tasks_id(wunderlist, 240932488)

for task in id_list:
    wunderpy.delete_tasks(wunderlist, task)
    time.sleep(0.5)

for title, date in zip(titles, dates):
    due_date = "20" + date[5:13]
    wunderpy.post_list(wunderlist, title, due_date, 240932488)
    time.sleep(0.5)
