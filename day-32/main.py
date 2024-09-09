import datetime as dt
import random

quotes_list = []
random_pick = 0


def quote_picker():
    global quotes_list, random_pick
    random_pick = 0
    with open("quotes.txt", mode="r") as f:
        quotes_list = [x for x in f.readlines()]
    random_pick += random.randint(0, len(quotes_list) - 1)
    return random_pick


quote_picker()

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

# date_of_birth = dt.datetime(year=1995, month=12, day=15)

if day_of_week == 0:
    import smtplib

    my_email = "patilaniket209@gmail.com"
    password = "zepu snzt qpij rtin"

    conn = smtplib.SMTP("smtp.gmail.com")
    conn.starttls()
    conn.login(user=my_email, password=password)
    conn.sendmail(
        from_addr=my_email,
        to_addrs="freeskincs@gmail.com",
        msg=f"Subject:Today's Quote.\n\n{quotes_list[random_pick]}.")
    conn.close()

