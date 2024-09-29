import time
import schedule

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")


time.sleep(5)

language_id = driver.find_element(By.ID, value="langSelect-EN")
language_id.click()

time.sleep(5)

cookie = driver.find_element(By.ID,value="bigCookie")
product0 = driver.find_element(By.ID,value="product0")
clicker_on = True
while clicker_on:
    cookie.click()
    try:
        schedule.every(5).seconds.do(product0.click())
    except:
        continue
    else:
        continue





# driver.find_element(By.ID,value="bigCookie").click()