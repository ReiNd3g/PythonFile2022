import telegram
from telegram.ext import CommandHandler, Updater

# Define the command that the bot will respond to
def download(update, context):
    # Replace this URL with the URL of the file you want to provide a download link for
    download_url = "bit.ly/MIAS01"
    # Send the download URL to the user
    context.bot.send_message(chat_id=update.message.chat_id, text=download_url)

# Create a CommandHandler for the "download" command
download_handler = CommandHandler('download', download)

# Set up the bot and start listening for user requests
updater = Updater(token='6289497302:AAE33ls_PiFzBSRGHU7SQ-6uV7MGLFJK-Zs', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(download_handler)
updater.start_polling()
