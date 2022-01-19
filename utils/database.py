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
    db = sqlite3.connect(DATABASE_FILE)
    cur = db.cursor()
    cur.execute("""SELECT LANGUAGE FROM User WHERE ID = ?""", (user_id,))
    user_lang = cur.fetchone()[0]
    db.close()
    if user_lang:
        return user_lang
    else:
        add_user(user_id)
        return 0


def get_user_voice_lang(user_id):
    db = sqlite3.connect(DATABASE_FILE)
    cur = db.cursor()

    cur.execute("""SELECT VOICE_LANG FROM User WHERE ID = ?""", (user_id,))
    voice_lang = cur.fetchone()[0]
    db.close()
    if voice_lang:
        return voice_lang
    else:
        add_user(user_id)
        return 0


def add_user(user_id, default = 'ENG'):
    db = sqlite3.connect(DATABASE_FILE)
    cur = db.cursor()
    cur.execute("""INSERT INTO User(ID, VOICE_LANG, LANGUAGE) VALUES (?, ?, ?)""", (user_id, default, default))
    db.commit()
    db.close()


def update_user_lang(user_id, lang):
    db = sqlite3.connect(DATABASE_FILE)
    cur = db.cursor()
    # exception if user is not in database
    cur.execute("""UPDATE TABLE User SET LANGUAGE = ? WHERE ID = ?""", (lang, user_id))
    db.close()


def update_user_voice_lang(user_id, lang):
    db = sqlite3.connect(DATABASE_FILE)
    cur = db.cursor()
    # exception if user is not in database
    cur.execute("""UPDATE TABLE User SET VOICE_LANG = ? WHERE ID = ?""", (lang, user_id))
    db.close()


if __name__ == '__main__':
    recreate_db()