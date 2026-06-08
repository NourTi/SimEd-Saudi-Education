"""
SimEd Multi-Platform Bot Launcher
"""

import os
import sys
import threading

from dotenv import load_dotenv

load_dotenv()


def main():
    """Start all bots based on environment variables"""

    platform = os.getenv("PLATFORM", "all").lower()

    if platform in ["discord", "all"]:
        if os.getenv("DISCORD_TOKEN"):
            print("🚀 Starting Discord bot...")
            from connectors.discord_bot import run_discord

            threading.Thread(
                target=run_discord, args=(os.getenv("DISCORD_TOKEN"),), daemon=True
            ).start()

    if platform in ["slack", "all"]:
        if os.getenv("SLACK_BOT_TOKEN"):
            print("🚀 Starting Slack bot...")
            from connectors.slack_bot import run_slack

            run_slack(os.getenv("SLACK_BOT_TOKEN"), os.getenv("SLACK_APP_TOKEN"))

    if platform in ["telegram", "all"]:
        if os.getenv("TELEGRAM_TOKEN"):
            print("🚀 Starting Telegram bot...")
            from connectors.telegram_bot import run_telegram

            run_telegram(os.getenv("TELEGRAM_TOKEN"))

    if platform in ["whatsapp", "all"]:
        if os.getenv("TWILIO_ACCOUNT_SID"):
            print("🚀 Starting WhatsApp bot...")
            from connectors.whatsapp_bot import run_whatsapp

            run_whatsapp()

    # Keep running
    while True:
        pass


if __name__ == "__main__":
    main()
