"""
Configuration management
"""

import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    # Platform tokens
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
    SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

    # Twilio (WhatsApp)
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

    # App settings
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    DEBUG = ENVIRONMENT == "development"
