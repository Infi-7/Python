import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
KEY = "SMGP7G69BBHNJ5OY"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the
# day before yesterday then print("Get News").

response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={KEY}")
data_open_yesterday = response.json()["Time Series (Daily)"]['2024-09-13']['1. open']
data_close_day_before_yesterday = response.json()["Time Series (Daily)"]['2024-09-13']['4. close']

print(data_open_yesterday)
print(data_close_day_before_yesterday)
print(((round(float(data_close_day_before_yesterday)) -
        round(float(data_open_yesterday)))
       /round(float(data_close_day_before_yesterday)))*100)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces
# for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's
# title and description to your phone number.


#Optional: Format the SMS message like this:

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

