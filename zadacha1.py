import telebot
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, Filters, MessageHandler, BaseFilter


token='5560578070:AAGUfikEyc5CjsjWXjxbECrsKvL5OVeOCYU'
bot = telebot.TeleBot(token)
GROUP_ID=1236915906
blacklist=['абв']

@bot.message_handler(content_types=["text"])
def handle_text(message):
    for x in blacklist:
        if(x in message.text):
            bot.delete_message(message.chat.id, message.message_id)
        else:
            pass

if __name__ == "__main__":
    bot.infinity_polling()

