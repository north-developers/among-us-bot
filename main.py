import telebot

import config
from sticker import among_us
  

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def handle_help(message):
    bot.send_message(message.chat.id, "*How to use:*\n\n/among <text>",  parse_mode = "Markdown")


@bot.message_handler(commands=['among'])
def handle_among(message):
    user_text = message.text
    text__ = " ".join(user_text.split()[1::])

    bot.send_sticker(message.chat.id, among_us(text__))
    print("[INFO] new sticker")

if __name__ == '__main__':
    bot.polling(none_stop=True)
