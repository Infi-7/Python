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

def looker():
    enables_list = []
    for enables in driver.find_elements(By.CSS_SELECTOR, value=".storeSection div"):
        if enables.get_attribute("class") == "product unlocked enabled":
            enables_list.append(enables.get_attribute('id'))
            print(enables_list)
            driver.find_element(By.ID,value=f"{enables_list[-1]}").click()

clicker_on = True
while clicker_on:
    cookie.click()
    try:
        schedule.every(10).seconds.do(looker())
    finally:
        continue

