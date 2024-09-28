from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

dic = {}
def value_extractor():
    for x in range(5):
        x += 1
        date = driver.find_element(By.XPATH,value=f"/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[{x}]/time").get_attribute("datetime")[:10]
        event = driver.find_element(By.XPATH, value=f"/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li[{x}]/a").text

        dic.update({x-1:{"date":date, "name":event}})

value_extractor()
print(dic)

driver.quit()
