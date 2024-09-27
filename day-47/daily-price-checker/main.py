import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

product_name = []
URL = os.getenv("WEBSITE_URL")
MY_EMAIL = os.getenv("SMTP_EMAIL")
MY_PASSWORD = os.getenv("SMTP_PASSWORD")

response = requests.get(URL,headers={"Accept-Language":"en-US",
                                     "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0"})
response_text = response.text

soup = BeautifulSoup(response_text, "html.parser")
print(soup.prettify())

product_name.append(' '.join(x for x in soup.find(name="span", class_="a-size-large product-title-word-break").getText().split()))
before_decimal = soup.find(name="span", class_="a-price-whole").getText()
after_decimal = soup.find(name="span", class_="a-price-fraction").getText()
current_price = float(f'{before_decimal}{after_decimal}')

print(product_name[0])
print(current_price)

if current_price < 100:
    print("True")

# Email sender setup
    
    con = smtplib.SMTP("smtp.gmail.com")
    con.starttls()
    con.login(MY_EMAIL, MY_PASSWORD)
    con.sendmail(
    from_addr=MY_EMAIL,
    to_addrs=MY_EMAIL,
    msg=f"{product_name} is now {current_price}")


