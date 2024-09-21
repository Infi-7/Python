import os
from twilio.rest import Client
import smtplib

# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        self.client = Client('ACc145f1feaf6961edc7fddce6fa276666', "4c92718940e917ade54ade0664e5b6a4")
        self.my_email = "patilaniket209@gmail.com"
        self.password = "zepu snzt qpij rtin"

    def send_emails(self, message_body):
        conn = smtplib.SMTP("smtp.gmail.com")
        conn.starttls()
        conn.login(user=self.my_email, password=self.password)
        conn.sendmail(
            from_addr=self.my_email,
            to_addrs="freeskincs@gmail.com",
            msg=message_body)
        conn.close()



'''
    def send_sms(self, message_body):
        """
        Sends an SMS message through the Twilio API.
        This function takes a message body as input and uses the Twilio API to send an SMS from
        a predefined virtual number (provided by Twilio) to your own "verified" number.
        It logs the unique SID (Session ID) of the message, which can be used to
        verify that the message was sent successfully.

        Parameters:
        message_body (str): The text content of the SMS message to be sent.

        Returns:
        None

        Notes:
        - Ensure that `TWILIO_VIRTUAL_NUMBER` and `TWILIO_VERIFIED_NUMBER` are correctly set up in
        your environment (.env file) and correspond with numbers registered and verified in your
        Twilio account.
        - The Twilio client (`self.client`) should be initialized and authenticated with your
        Twilio account credentials prior to using this function when the Notification Manager gets
        initialized.
        """
        message = self.client.messages.create(
            from_=["+12073557430"],
            body=message_body,
            to=["+917720834048"]
        )
        # Prints if successfully sent.
        print(message.sid)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
'''


