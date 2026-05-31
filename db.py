import sqlite3

DB_PATH = "news.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        articles TEXT,
        headline TEXT,
        art_date TEXT,
        link TEXT,
        content TEXT
    )
    """)
    conn.commit()
    conn.close()

def insert_news(articles, headline, art_date, link, content):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO news (articles, headline, art_date, link, content)
        VALUES (?, ?, ?, ?, ?)
        """,
        (articles, headline, art_date, link, content)
    )
    conn.commit()
    conn.close()
