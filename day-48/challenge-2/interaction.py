from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.CSS_SELECTOR, value="a[title='Special:Statistics']").text
# print(article_count)

# all_portals = driver.find_element(By.LINK_TEXT,value="Content portals")
# all_portals.click()

search_button = driver.find_element(By.CSS_SELECTOR,value="a[href='/wiki/Special:Search']")
search_button.click()

search = driver.find_element(By.NAME,value="search")
search.send_keys("Python", Keys.ENTER)



# driver.quit()