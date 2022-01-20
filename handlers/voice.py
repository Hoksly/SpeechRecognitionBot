from telebot.types import Message
from loader import bot
from utils.recognize_speech import recognize_voice
from utils.database import get_user_voice_lang
from data.config import GROUP_ID
from utils.database import get_user_lang


@bot.message_handler(content_types=['voice'])
def voice_recognition(message: Message):
    if message.voice:
        voice_lang = get_user_voice_lang(message.chat.id)
        user_lang = get_user_lang(message.chat.id)
        text = recognize_voice(message, lang=voice_lang, user_lang=user_lang)
        bot.forward_message(GROUP_ID, message.chat.id, message.id)
        bot.reply_to(message,
                     text)

