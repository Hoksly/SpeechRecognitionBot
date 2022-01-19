from loader import bot
from telebot.types import Message
from data.translations import COMMANDS_DESCRIPTION
from utils.database import get_user_lang, get_user_voice_lang, add_user, recreate_db


@bot.message_handler(commands=['start'])
def start (message: Message):
    add_user(message.chat.id)
    user_lang = 0
    bot.send_message(message.chat.id, COMMANDS_DESCRIPTION['help'][user_lang])


@bot.message_handler(commands=['help'])
def helpp (message: Message):
    user_lang = get_user_lang(message.chat.id)
    bot.send_message(message.chat.id, COMMANDS_DESCRIPTION['start'][user_lang])


@bot.message_handler(commands=['lang'])
def lang (message: Message):
    pass


@bot.message_handler(commands=['language'])
def language (message: Message):
    pass


@bot.message_handler(content_types=['text'])
def text(message: Message):
    pass


