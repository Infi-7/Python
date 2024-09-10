##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import pandas as pd

now = dt.datetime.now()
year = now.year
day = now.day
month = now.month

df = pd.read_csv("birthdays.csv")
convert_to_df = pd.DataFrame(df)
for x in convert_to_df["day"]:
    for y in convert_to_df["month"]:
        if x == day and y == month:
            print(x, y)


for x in range(len(convert_to_df["day"])):
    for y in range(len(convert_to_df["month"])):
        if x == y:
            print("true")

"""
my_email = "patilaniket209@gmail.com"
password = "zepu snzt qpij rtin"

conn = smtplib.SMTP("smtp.gmail.com")
conn.starttls()
conn.login(user=my_email, password=password)
conn.sendmail(
    from_addr=my_email,
    to_addrs="freeskincs@gmail.com",
    msg=f"Subject:Birthday Wishes.\n\nHappy Birthday!!!.")
conn.close()
"""
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




