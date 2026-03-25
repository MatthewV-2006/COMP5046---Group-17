import sqlite3

conn = sqlite3.connect("medications.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS medications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    dose TEXT NOT NULL, 
    reminder_time TEXT NOT NULL,
    child_ID INTEGER
    )""")

conn.commit()

def add_med_to_db(name, dose, reminder_time, child_id):
    cursor.execute("INSERT INTO medications (name, dose, reminder_time, child_ID) VALUES (?, ?, ?, ?)", (name, dose, reminder_time, child_id))
    conn.commit()

def get_med_db():
    cursor.execute("SELECT child_ID, name, dose, reminder_time FROM medications")
    return cursor.fetchall()