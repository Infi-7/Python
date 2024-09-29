from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, value="a[title='Special:Statistics']").text
# print(article_count)

all_portals = driver.find_element(By.LINK_TEXT,value="Content portals")
all_portals.click()


# driver.quit()