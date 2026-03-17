import sqlite3

conn = sqlite3.connect("medications.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS medications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    DOSE TEXT NOT NULL, 
    reminder_time TEXT NOT NULL)""")
conn.commit()

def add_med_to_db(name, dose, reminder_time):
    cursor.execute(
        "INSERT INTO medications (name, dose, reminder_time) VALUES (?, ?, ?)",
        (name, dose, reminder_time)
    )
    conn.commit()

def get_med_db():
    cursor.execute("SELECT name, dose, reminder_time FROM medications")
    return cursor.fetchall()