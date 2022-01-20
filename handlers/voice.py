from telebot.types import Message
from loader import bot
from utils.recognize_speech import recognize_voice
from utils.database import get_user_voice_lang


@bot.message_handler(content_types=['voice'])
def voice_recognition(message: Message):
    if message.voice:
        voice_lang = get_user_voice_lang(message.chat.id)
        text = recognize_voice(message, lang=voice_lang)

        bot.reply_to(message,
                     text)

