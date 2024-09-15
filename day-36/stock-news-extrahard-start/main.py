import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_KEY = "SMGP7G69BBHNJ5OY"
NEWS_KEY = "98ae469ce4c24af1b5694f7f2e677c9b"

SEND_TITLE = ""
SEND_DESC = ""

account_sid = "ACc145f1feaf6961edc7fddce6fa276666"
auth_token = "4c92718940e917ade54ade0664e5b6a4"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the
# day before yesterday then print("Get News").

stock_response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={STOCK_KEY}")
data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
data_yesterday = data_list[0]
data_yesterday_close = float(data_yesterday["4. close"])

data_day_before_yesterday = data_list[1]
data_day_before_yesterday_close = float(data_day_before_yesterday["4. close"])

difference = data_yesterday_close - data_day_before_yesterday_close

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces
# for the COMPANY_NAME.

per = round((difference / data_yesterday_close) * 100)
if abs(per) > 1:
    news_response = requests.get('https://newsapi.org/v2/everything?'
           f'q={COMPANY_NAME}&'
           'language=en&'
           'sortBy=publishedAt&'
           'apiKey=98ae469ce4c24af1b5694f7f2e677c9b')

    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)

    # STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's
    # title and description to your phone number.
    formatted_articles = [f"Headline: {article['title']}. \n{article['description']}" for article in three_articles]

    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            body=f"{article}",
            from_="+12073557430",
            to="+917720834048",
        )

# Optional: Format the SMS message like this:

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
