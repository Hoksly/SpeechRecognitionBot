from data.config import DATABASE_FILE
import sqlite3


def recreate_db():
    db = sqlite3.connect(DATABASE_FILE)
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS User(
            ID INT PRIMARY KEY,
            VOICE_LANG TEXT,
            LANGUAGE TEXT
    )""")
    db.commit()
    db.close()


def get_user_lang(user_id):
    pass


def get_user_voice_lang(user_id):
    pass


def add_user(user_id):
    pass


def update_user_lang(user_id, lang):
    pass


def update_user_voice_lang(user_id, lang):
    pass


