import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETS_LINK = os.getenv("sheets_link")
SHEETS_LINK2 = os.getenv("sheets_link2")
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

driver2 = webdriver.Chrome(options=chrome_options)
driver2.get(SHEETS_LINK2)

minor_address = driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
minor_price = driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
minor_links = driver.find_element(By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
minor_submit_clicker = driver.find_element(By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div")




major_address = driver2.find_element(By.XPATH,"//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
major_price = driver2.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
major_links = driver2.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
major_submit_clicker = driver2.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div")


for entry in range(len(prop_address)):
    if entry == 0:
        minor_address.send_keys(prop_address[entry])
        minor_price.send_keys(prop_price[entry])
        minor_links.send_keys(prop_links[entry])
        minor_submit_clicker.click()


    else:
        major_address.send_keys(prop_address[entry])
        major_price.send_keys(prop_price[entry])
        major_links.send_keys(prop_links[entry])
        major_submit_clicker.click()

    if entry < len(prop_address) - 1:
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "body > div.Uc2NEf > div:nth-child(2) > div.RH5hzf.RLS9Fe > div > div.c2gzEf > a").click()
        time.sleep(5)
