from config import TOKEN, BOT_USERNAME
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import requests
# Commands

async def start_Cmd(update : Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello there, Welcome to MimicMe Bot.")

async def joke_Cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get("https://v2.jokeapi.dev/joke/Any?safe-mode")
    data = response.json()

    if data["type"] == "single":
        await update.message.reply_text(f"{data["joke"]}")

    else:
        await update.message.reply_text(f"{data['setup']}\n\n{data['delivery']}")



async def help_Cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("MimicMe Bot will just Mimic what you said in mocking way. And it'll tell you some random jokes.")

# Functions

async def Mimic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    first_name = update.message.from_user.first_name
    message = update.message.text
    await update.message.reply_text(f'I think {first_name} said \"{message}\", but I do not care! \U0001F913\U0000261D\U0001F3FB')

# Main func call

if __name__ == "__main__":
        app = ApplicationBuilder().token(TOKEN).build()
        print("Starting...")

# Commands connection

        app.add_handler(CommandHandler("start", start_Cmd))
        app.add_handler(CommandHandler("help", help_Cmd))
        app.add_handler(CommandHandler("joke", joke_Cmd))

        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, Mimic))


        print("Polling...")
        app.run_polling()
