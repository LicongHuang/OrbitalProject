import sqlite3

conn = sqlite3.connect('passcode.db')
cur = conn.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS passcode (
                id INTEGER PRIMARY KEY,
                usb_id TEXT,
                pass BLOB)
            """)

conn.commit()

