from telebot import TeleBot

from nfstt.config import telbot_token

bot = TeleBot(telbot_token)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id,
                     f"Привет, {message.chat.username}! \nДля получения ID текущего чата необходимо ввести команду /getchatid")

@bot.message_handler(commands=['getchatid'])
def get_chatid(message):
    bot.send_message(message.chat.id,
                     f"ID данного чата: {message.chat.id}")

bot.polling(none_stop=True)