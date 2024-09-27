import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://appbrewery.github.io/instant_pot/"
product_name = []
MY_EMAIL = "patilaniket209@gmail.com"
MY_PASSWORD = "zepu snzt qpij rtin"

response = requests.get(URL)
response_text = response.text

soup = BeautifulSoup(response_text, "html.parser")
product_name.append(' '.join(x for x in soup.find(name="span", class_="a-size-large product-title-word-break").getText().split()).encode('utf-8'))
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
