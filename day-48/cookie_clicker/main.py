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

enables_list = {}
cookie = driver.find_element(By.ID,value="bigCookie")

# upgrade_section = driver.find_element(By.ID, value="products0")

# schedule.every(5).seconds.do(looker())
'''
test = driver.find_element(By.CSS_SELECTOR, value=".storeSection div")
print(test)
'''
def looker():
    enables_list.clear()
    for enables in driver.find_elements(By.CSS_SELECTOR, value=".storeSection div"):
        if enables.get_attribute("class") == "product unlocked enabled":
            price = driver.find_element(By.CSS_SELECTOR, value=".storeSection div div .price").text
            enables_list.update({enables.get_attribute('id'):price})
            print(enables_list)




clicker_on = True
while clicker_on:
    cookie.click()

    try:
        schedule.every(10).seconds.do(looker())
    except:
        continue
    else:
        continue
