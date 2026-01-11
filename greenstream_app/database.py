import sqlite3

DB_NAME = "notes.db"

# Reuse a single connection (green practice)
_connection = None

def get_connection():
    global _connection
    if _connection is None:
        _connection = sqlite3.connect(DB_NAME, check_same_thread=False)
    return _connection

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT
        )
    """)
    conn.commit()
