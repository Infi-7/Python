import requests
from twilio.rest import Client


class NotificationManager:
    def __init__(self, body):
        self.SID = "ACc145f1feaf6961edc7fddce6fa276666"
        self.TOKEN = "4c92718940e917ade54ade0664e5b6a4"
        self.body = body

    def notifier(self):
        client = Client(self.SID, self.TOKEN)
        message = client.messages.create(
            body=f"{self.body}",
            from_="+12073557430",
            to="+917720834048",
        )
