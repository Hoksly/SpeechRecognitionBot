import speech_recognition as sr
from data.config import LANGUAGES
from utils.saver import save_voice_file
import os


def recognize(filename, lang = 'RU'):
    r = sr.Recognizer()

    recog = sr.Recognizer()
    sample_audio = sr.AudioFile(filename)
    with sample_audio as audio_file:
        audio_content = recog.record(audio_file)

    return recog.recognize_google(audio_content, language=LANGUAGES[lang])


async def recognize_voice(message, lang = 'RU'):
    filename = await save_voice_file(message)
    text = recognize(filename, lang=lang)
    os.remove(filename)
    return text