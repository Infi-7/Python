import smtplib

my_email = "patilaniket209@gmail.com"
password = "zepu snzt qpij rtin"

conn = smtplib.SMTP("smtp.gmail.com")
conn.starttls()
conn.login(user=my_email, password=password)
conn.sendmail(
    from_addr=my_email,
    to_addrs="freeskincs@gmail.com",
    msg="Subject:Hello\n\nBody.")
conn.close()
