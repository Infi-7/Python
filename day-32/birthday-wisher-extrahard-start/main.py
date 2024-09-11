##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd

now = dt.datetime.now()
year = now.year
day = now.day
month = now.month
current_year = 0
receiver_email = ""

df = pd.read_csv("birthdays.csv")
convert_to_df = pd.DataFrame(df)
convert_to_dict = convert_to_df.to_dict("split")


def email_retriever():
    global current_year, receiver_email
    current_year = 0
    receiver_email = ''
    for x in convert_to_dict["index"]:
        if convert_to_dict["data"][x][4] == day and convert_to_dict["data"][x][5] == month:
            current_year = convert_to_dict["data"][x][6]
            receiver_email += convert_to_dict["data"][x][3]


email_retriever()

my_email = "patilaniket209@gmail.com"
password = "zepu snzt qpij rtin"

conn = smtplib.SMTP("smtp.gmail.com")
conn.starttls()
conn.login(user=my_email, password=password)
conn.sendmail(
    from_addr=my_email,
    to_addrs="freeskincs@gmail.com",
    msg=f"Subject:Birthday Wishes.\n\nHappy {year - current_year} Birthday!!!.")
conn.close()

