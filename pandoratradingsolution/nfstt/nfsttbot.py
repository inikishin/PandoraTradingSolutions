"""
Данный модуль позволяет отправлять сообщения в Telegram, в заданный список чатов. Чаты указываются в файле config.py.

Доступные функции:

send_notification(message) - отправка сообщения message

"""


from telebot import TeleBot

from nfstt.config import telbot_token, chat_ids, site_descr


def send_notification(message):
    bot = TeleBot(telbot_token)
    msg = f'С сайта {site_descr["site_name"]} получено следующее сообщение:\n {message}'
    for c in chat_ids:
        bot.send_message(c, msg)

