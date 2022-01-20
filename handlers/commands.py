from loader import bot
from telebot.types import Message
from data.translations import COMMANDS_DESCRIPTION
from utils.database import get_user_lang, get_user_voice_lang, add_user, recreate_db
import telebot
from data.translations import VOICE_LANGUAGES, COMMANDS_DESCRIPTION, LANGUAGES


@bot.message_handler(commands=['start'])
def start (message: Message):
    recreate_db()
    add_user(message.chat.id)
    user_lang = 0
    bot.send_message(message.chat.id, COMMANDS_DESCRIPTION['start'][user_lang])


@bot.message_handler(commands=['help'])
def helpp (message: Message):
    user_lang = get_user_lang(message.chat.id)
    bot.send_message(message.chat.id, COMMANDS_DESCRIPTION['help'][user_lang])


@bot.message_handler(commands=['lang'])
def lang(message: Message):
    try:
        user_lang = get_user_lang(message.chat.id)

        markup = telebot.types.InlineKeyboardMarkup()

        for i in range(len(VOICE_LANGUAGES[user_lang])):
            markup.add(telebot.types.InlineKeyboardButton(VOICE_LANGUAGES[user_lang][i][0], callback_data='V' + str(i)))
        bot.send_message(message.chat.id, COMMANDS_DESCRIPTION['lang'][user_lang], reply_markup=markup)

    except Exception as e:
        print ('\x1b[0;30;41m' + "Error in lang(): {} !".format(e) + '\x1b[0m')


@bot.message_handler(commands=['language'])
def language (message: Message):
    user_lang = get_user_lang(message.chat.id)

    markup = telebot.types.InlineKeyboardMarkup()
    for i in range(len(LANGUAGES[user_lang])):
        markup.add(telebot.types.InlineKeyboardButton(LANGUAGES[user_lang][i], callback_data='L' + str(i)))
    bot.send_message(message.chat.id, COMMANDS_DESCRIPTION['language'][user_lang], reply_markup=markup)


@bot.message_handler(commands=['cid'])
def cid (messsage):
    bot.send_message (messsage.chat.id, messsage.chat.id)


@bot.message_handler(content_types=['text'])
def text(message: Message):
   pass



