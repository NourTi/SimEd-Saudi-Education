"""
Telegram connector for SimEd Studio Bot
"""

from core.agent import SimEdAgent
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

agent = SimEdAgent()


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    user_id = str(update.effective_user.id)
    response = agent.start_conversation(user_id)
    await update.message.reply_text(response)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming messages"""
    user_id = str(update.effective_user.id)
    message_text = update.message.text

    response = agent.process_message(user_id, message_text)
    await update.message.reply_text(response)


def run_telegram(token: str):
    """Start Telegram bot"""
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Telegram bot started")
    app.run_polling()
