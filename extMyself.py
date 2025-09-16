#! python3
# textMyself.py - Defines the textmyself() function that texts a message  passed to it as a string.

# Preset values:
accountSID = input("Enter account SID\n")
authToken = input("Enter auth token\n")
myNumber = input("Enter number to send SMS to\n")
twilioNumber = input("Enter twilio Number\n")

from twilio.rest import Client


def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)


textmyself("The Boring Task is finished")
