import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_KEY = "SMGP7G69BBHNJ5OY"
NEWS_KEY = "98ae469ce4c24af1b5694f7f2e677c9b"
SEND_TITLE = ""
SEND_DESC = ""

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the
# day before yesterday then print("Get News").

# stock_response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={KEY}")
data_open_yesterday = 228.0000  # float(stock_response.json()["Time Series (Daily)"]['2024-09-13']['1. open'])
data_close_day_before_yesterday = 230.2900  # float(stock_response.json()["Time Series (Daily)"]['2024-09-13']['4. close'])

per = ((data_open_yesterday - data_close_day_before_yesterday) / data_open_yesterday) * 100
STOCK_STATUS = ""
if per > 0:
    print(f"{STOCK} 🔺{round(per)}%")
elif per < 0:
    print(f"{STOCK}🔻{abs(round(per))}%")
elif per == 0:
    print(f"No changes.")


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces
# for the COMPANY_NAME.
'''
news_response = requests.get('https://newsapi.org/v2/everything?'
       'q=tesla&'
       'from=2024-08-14&'
       'language=en&'
       'sortBy=publishedAt&'
       'apiKey=98ae469ce4c24af1b5694f7f2e677c9b')

for x in range(3):
    SEND_TITLE = ""
    SEND_DESC = ""
    print(news_response.json()["articles"][x]["title"])
    print(news_response.json()["articles"][x]["description"])
    print("-----------------------------------------------------------")
'''

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's
# title and description to your phone number.

account_sid = "ACc145f1feaf6961edc7fddce6fa276666"
auth_token = "4c92718940e917ade54ade0664e5b6a4"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body=f"{STOCK_STATUS}\nHeadline: {SEND_TITLE}\nBrief: {SEND_DESC}",
    from_="+12073557430",
    to="+917720834048",
)

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

