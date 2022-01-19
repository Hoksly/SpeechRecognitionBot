from aiogram import types
from loader import bot
from utils.recognize_speech import recognize_voice


@bot.message_handler(content_types=['voice'])
def idk_how_to_name_you(message: types.Message):
    if message.voice:

        text = recognize_voice(message, lang = 'UKR')
        bot.send_message(message.chat.id, text)

