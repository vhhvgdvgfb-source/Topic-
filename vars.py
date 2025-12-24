#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "24223199"))
API_HASH = environ.get("API_HASH", "37e36927e2b89c00ed0ec91ef0aa3eaa")
BOT_TOKEN = environ.get("BOT_TOKEN", "8560070727:AAHPVi4LrahBFY-UI0DH7J0ZP0k4hEbtJMI")

OWNER = int(environ.get("OWNER", "8454559384"))
CREDIT = environ.get("CREDIT", "KITTU 𝘽𝙊𝙏𝙎")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8454559384').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '6658266490').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set



