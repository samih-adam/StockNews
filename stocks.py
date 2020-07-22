# Goal of today is to automate text messages for
# stock news and also stock fundamentals for a friend of mine who is a broker

from twilio.rest import Client

account_sid = '####'
auth_token = '###'
client = Client(account_sid, auth_token)


def send_news():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hola baby this is being sent via code',
        to='whatsapp:+###'
    )

    print(message.sid)
