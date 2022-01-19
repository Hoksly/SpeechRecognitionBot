from aiogram import types
from loader import dp, bot
from utils.recognize_speech import recognize_voice


@dp.message_handler(content_types=[types.ContentType.VOICE])
async def idk_how_to_name_you(message: types.Message):
    if message.voice:

        text = await recognize_voice(message, lang = 'UKR')
        await bot.send_message(message.chat.id, text)

