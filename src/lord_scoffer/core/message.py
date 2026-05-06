from twilio.rest import Client
from config.settings import settings

client = Client(
    settings.TWILIO_ACCOUNT_SID, 
    settings.TWILIO_AUTH_TOKEN
    )

def send_message(phone_number: str, message: str):
    message = client.messages.create(
        body=message,
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone_number
    )
    return message.sid