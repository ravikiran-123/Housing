# from django.conf import settings
# from twilio.rest import Client
# import random

# class MessaHandler:

#     phone_number=None
#     otp=None

#     def __init__(self, phone_number, otp) ->None:
#         self.phone_number=phone_number
#         self.otp=otp

#     def send_otp_on_phone(self):

#         client=Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)

#         message=client.messages.create(
#                                         body=f'Your otp is{self.otp}',
#                                         from_='+13254132877',
#                                         to=self.phone_number,
#         )

#         print(message.sid)

import random
import requests

def generate_otp():
    return str(random.randint(1000, 9999))  # Generate a random 4-digit OTP

def send_otp_via_textlocal(api_key, sender, phone_number, otp):
    # import pdb
    # pdb.set_trace()
    message = f"Your OTP is: {otp}"
    url = "https://api.textlocal.in/send/"
    params = {
        'apiKey': api_key,
        'sender': sender,
        'numbers': phone_number,
        'message': message,
    }

    response = requests.get(url, params=params)
    return response.json()

def verify_otp(user_otp, generated_otp):
    return user_otp == generated_otp
