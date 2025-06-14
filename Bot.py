   # bot.py
   from telegram import Update
   from telegram.ext import Updater, CommandHandler, CallbackContext

   # Define a command handler
   def start(update: Update, context: CallbackContext) -> None:
       update.message.reply_text('Hello! I am your bot.')

   def main():
       # Replace 'YOUR_TOKEN' with your actual bot token
       updater = Updater("7783848430:AAEYKCoNpZnJEOTYVuawYgr9bC1N3QE5jfY")

       # Register the command handler
       updater.dispatcher.add_handler(CommandHandler("start", start))

       # Start the bot
       updater.start_polling()
       updater.idle()

   if __name__ == '__main__':
       main()
   
