import tkinter as tk
import sqlite3

def login():
    login_button.pack_forget()

    tk.Label(root, text="Username").pack()
    username_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry.pack()

    submit_button.pack()

def submit():
    username = username_entry.get()
    password = password_entry.get()
    sql = '''INSERT INTO AccountDetails(AccountID,username,password,isAdmin)
             VALUES(?,?,?,?) '''
    sqlGetID = 'SELECT AccountID from AccountDetails ORDER BY AccountID DESC LIMIT 1'
    
    
    
    with sqlite3.connect('Details.db') as conn:
        cursor = conn.cursor()
        cursor.execute(sqlGetID)
        getId = cursor.fetchone()[0]
        Id = int(getId)+1
        info = (Id, username, password, False)

        cursor.execute(sql, info)



root = tk.Tk()
root.title("Login")
root.geometry("400x300")

login_button = tk.Button(root, text="Login", command=login, width=10)
login_button.pack()

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

submit_button = tk.Button(root, text="Submit", command=submit, width=10)
root.mainloop()
