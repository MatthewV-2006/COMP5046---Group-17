import tkinter as tk
import sqlite3

def login():
    login_button.pack_forget()

    tk.Label(root, text="Username").pack()
    username_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry.pack()
    create_button.pack()
    submit_button.pack()

def submit():
    username = username_entry.get()
    password = password_entry.get()
    sql = '''SELECT * FROM AccountDetails WHERE username=?'''
    with sqlite3.connect('Details.db') as conn:
        cursor = conn.cursor()
        cursor.execute(sql,(username,))
        row = cursor.fetchall()
        print(row)
        print(username)
        print(password)
        if(row != []):
            fetchedID = row[0][0]
            fetchedUsername = row[0][1]
            fetchedPassword = row[0][2]
            fetchedAdminStatus = row[0][3]
            if((fetchedUsername == username) and (fetchedPassword==password)):
                return([fetchedID,fetchedUsername,fetchedPassword,fetchedAdminStatus])
            else:
                return None

def createAccount():
    username = username_entry.get()
    password = password_entry.get()
    sql = '''INSERT INTO AccountDetails(AccountID,username,password,isAdmin)
             VALUES(?,?,?,?) '''
    sqlGetID = 'SELECT MAX(CAST(AccountID AS INTEGER)) FROM AccountDetails'

    
    
    
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

submit_button = tk.Button(root, text="Sign in", command=submit, width=10)

create_button = tk.Button(root, text="Create account", command=createAccount, width=10)
root.mainloop()
