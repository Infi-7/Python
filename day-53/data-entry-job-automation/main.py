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
    for c in driver.find_elements(By.CSS_SELECTOR, value=".Qr7Oae div div .AgroKb div div div input"):
        c.send_keys("hello")

    if x < LIMIT - 1:
        time.sleep(1)
        s = driver.find_element(By.CSS_SELECTOR, value=".lRwqcd div")
        s.click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, value=".c2gzEf a").click()


