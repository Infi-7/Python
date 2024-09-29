from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME,value="fName")
f_name.send_keys("a")

l_name = driver.find_element(By.NAME,value="lName")
l_name.send_keys("p")

email = driver.find_element(By.NAME,value="email")
email.send_keys("ap@example.com", Keys.ENTER)
