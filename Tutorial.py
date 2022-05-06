from telegram.ext import Updater, CommandHandler

def Start(update, context):
    update.effective_message.reply_text("Hello World!")

def main():
    updater = Updater("5301435865:AAFR7gB4GwHsIdBKm0EbRwWIkLuN64iz3Rs")
    updater.dispatcher.add_handler(CommandHandler("start", Start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()