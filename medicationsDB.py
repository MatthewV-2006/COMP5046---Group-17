import sqlite3

conn = sqlite3.connect("medications.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS medications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    DOSE TEXT NOT NULL, 
    reminder_time TEXT NOT NULL,
    child_ID INTEGER
    )""")

# adding a new column 'child_ID' to DB
# if child_ID doesn't exist then it's added otherwise it does nothing
try:
    cursor.execute("ALTER TABLE medications ADD COLUMN child_ID INTEGER")
except:
    pass

conn.commit()

def add_med_to_db(name, dose, reminder_time):
    cursor.execute("INSERT INTO medications (name, dose, reminder_time) VALUES (?, ?, ?)", (name, dose, reminder_time))
    conn.commit()

def get_med_db():
    cursor.execute("SELECT name, dose, reminder_time FROM medications")
    return cursor.fetchall()