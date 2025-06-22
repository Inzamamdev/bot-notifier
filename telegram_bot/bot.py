from telegram.ext import Application, CommandHandler
from django.conf import settings
from .models import TelegramUser
from asgiref.sync import sync_to_async

async def start(update, context):
    username = update.message.from_user.username
    if username:
        await sync_to_async(TelegramUser.objects.get_or_create)(username=username)
        await update.message.reply_text(f"Welcome, {username}! Your username has been saved.")
    else:
        await update.message.reply_text("Please set a Telegram username in your profile and try again.")

def run_bot():
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()