from aiogram import types
from data.translations import COMMANDS


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("help", COMMANDS['help'][0]),
            types.BotCommand("lang", COMMANDS['lang'][0]),
            types.BotCommand("language", COMMANDS['language'][0]),
        ]
    )
