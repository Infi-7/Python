import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETS_LINK = os.getenv("sheets_link")
response = requests.get("https://appbrewery.github.io/Zillow-Clone/").text
prop_price = []
prop_links = []
prop_address = []
LIMIT = 10

soup = BeautifulSoup(response, "html.parser")

# collect listing link
for x in soup.find_all(class_="StyledPropertyCardDataArea-anchor", limit=LIMIT):
    prop_links.append(x["href"])

# collect listing price
for x in soup.find_all(class_="PropertyCardWrapper__StyledPriceLine", limit=LIMIT):
    prop_price.append(x.text[:-4])

# collect listing address
for x in soup.find_all(class_="StyledPropertyCardDataArea-anchor", limit=LIMIT):
    prop_address.append(x.text.strip())

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(SHEETS_LINK)

for x in range(LIMIT):
    time.sleep(3)
    driver.find_element(By.XPATH, value='//input[@aria-describedby="i2 i3"]').send_keys(prop_address[x])
    driver.find_element(By.XPATH, value='//input[@aria-describedby="i6 i7"]').send_keys(prop_price[x])
    driver.find_element(By.XPATH, value='//input[@aria-describedby="i10 i11"]').send_keys(prop_links[x])

    time.sleep(1)
    s = driver.find_element(By.CSS_SELECTOR, value=".lRwqcd div")
    s.click()

    if x < LIMIT - 1:
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, value=".c2gzEf a").click()


