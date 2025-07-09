import os
from twilio.rest import Client
import re

# SMS Reminder Module (Twilio Integration)

def is_valid_phone_number(phone_number):
    """
    Validate phone number (E.164 format, basic area code check for +48/Poland or +1/US as example)
    """
    pattern = r'^\+\d{10,15}$'
    if not re.match(pattern, phone_number):
        return False
    # Example: allow only +48 (Poland) or +1 (US) for demo
    if not (phone_number.startswith('+48') or phone_number.startswith('+1')):
        return False
    return True

def is_opted_in(user_profile):
    """
    Check if user has opted in for SMS reminders (expects dict with 'sms_opt_in' key)
    """
    return user_profile.get('sms_opt_in', False)

def send_sms_reminder(phone_number, message, twilio_sid=None, twilio_auth=None, twilio_phone=None):
    """
    Send an SMS reminder using Twilio
    Args:
        phone_number (str): Recipient's phone number (E.164)
        message (str): Message to send
        twilio_sid (str): Twilio Account SID (optional, else from env)
        twilio_auth (str): Twilio Auth Token (optional, else from env)
        twilio_phone (str): Twilio phone number (optional, else from env)
    Returns:
        bool: True if sent, False otherwise
    """
    try:
        twilio_sid = twilio_sid or os.getenv('TWILIO_SID')
        twilio_auth = twilio_auth or os.getenv('TWILIO_AUTH')
        twilio_phone = twilio_phone or os.getenv('TWILIO_PHONE')
        if not (twilio_sid and twilio_auth and twilio_phone):
            print("Twilio credentials not set.")
            return False
        if not is_valid_phone_number(phone_number):
            print("Invalid phone number format.")
            return False
        client = Client(twilio_sid, twilio_auth)
        client.messages.create(
            to=phone_number,
            from_=twilio_phone,
            body=message
        )
        return True
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return False

def schedule_sms_reminder(user_profile, message, send_time):
    """
    Stub for scheduling SMS reminders (to be implemented with a scheduler or background job)
    Args:
        user_profile (dict): User profile with phone, opt-in, etc.
        message (str): Message to send
        send_time (datetime): When to send
    """
    # This would be implemented with a scheduler (e.g., APScheduler, cron, etc.)
    pass


