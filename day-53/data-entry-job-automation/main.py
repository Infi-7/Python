import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETS_LINK = os.getenv("sheets_link")
print(SHEETS_LINK)

response = requests.get("https://appbrewery.github.io/Zillow-Clone/").text
prop_price = []
prop_links = []
prop_address = []

soup = BeautifulSoup(response, "html.parser")

# collect listing link
for x in soup.find_all(class_="StyledPropertyCardDataArea-anchor", limit=10):
    prop_links.append(x["href"])

# collect listing price
for x in soup.find_all(class_="PropertyCardWrapper__StyledPriceLine", limit=10):
    prop_price.append(x.text[:-4])

# collect listing address
for x in soup.find_all(class_="StyledPropertyCardDataArea-anchor", limit=10):
    prop_address.append(x.text.strip())

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(SHEETS_LINK)

address = driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
price = driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
links = driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
submit_clicker = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div")

address.send_keys(prop_address[0])
price.send_keys(prop_price[0])
links.send_keys(prop_links[0])
submit_clicker.click()
