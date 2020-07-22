# Goal of today is to automate text messages for
# stock news and also stock fundamentals for a friend of mine who is a broker

from twilio.rest import Client

account_sid = 'AC93eeba79b2edbcc2f396430887d78f29'
auth_token = '7f5eb3e5c6951f87e6141ae4d651f169'
client = Client(account_sid, auth_token)


def send_news():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hola baby this is being sent via code',
        to='whatsapp:+13148289905'
    )

    print(message.sid)
