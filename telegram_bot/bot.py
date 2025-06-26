from telegram.ext import Application, CommandHandler
from django.conf import settings
from .models import TelegramUser
from django.core.exceptions import ObjectDoesNotExist

async def start(update, context):
    username = update.message.from_user.username
    if username:
        try:
            await TelegramUser.objects.aget(username=username)
            created = False
        except ObjectDoesNotExist:
            await TelegramUser.objects.acreate(username=username)
            created = True

        await update.message.reply_text(
            f"Welcome, {username}! Your username has {'been saved' if created else 'already been saved.'}"
        )
    else:
        await update.message.reply_text("Please set a Telegram username in your profile and try again.")

def run_bot():
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()