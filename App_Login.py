import tkinter as tk
import sqlite3

class loginPage:
    def __init__(self, root):
        for child in root.winfo_children():
            child.destroy()
        root.title("Login")
        root.geometry("400x300")
        self.userDetails = []
        self.closingAction = "quit"

    def main(self, root):
        login_button = tk.Button(root, text="Login", command=lambda: self.login(root, login_button, username_entry, password_entry, create_button, submit_button), width=10)
        login_button.pack()

        username_entry = tk.Entry(root)
        password_entry = tk.Entry(root, show="*")

        submit_button = tk.Button(root, text="Sign in", command=lambda: self.submit(root, username_entry, password_entry), width=10)

        create_button = tk.Button(root, text="Create account", command=lambda: self.createAccount(root, username_entry, password_entry), width=10)
        root.mainloop()
        return (self.userDetails,self.closingAction)


    def login(self, root, login_button, username_entry, password_entry, create_button, submit_button):
        login_button.pack_forget()

        tk.Label(root, text="Username").pack()
        username_entry.pack()

        tk.Label(root, text="Password").pack()
        password_entry.pack()
        create_button.pack()
        submit_button.pack()

    def submit(self, root, username_entry, password_entry):
        username = username_entry.get()
        password = password_entry.get()
        sql = '''SELECT * FROM AccountDetails WHERE username=?'''
        with sqlite3.connect('Details.db') as conn:
            cursor = conn.cursor()
            cursor.execute(sql,(username,))
            row = cursor.fetchall()
            if(row != []):
                fetchedID = row[0][0]
                fetchedUsername = row[0][1]
                fetchedPassword = row[0][2]
                fetchedAdminStatus = row[0][3]
                if((fetchedUsername == username) and (fetchedPassword==password)):
                    root.quit()
                    self.userDetails = [fetchedID,fetchedUsername,fetchedPassword,fetchedAdminStatus]
                    self.closingAction = "signInSuccess"

    def createAccount(self, root, username_entry, password_entry):
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
            self.userDetails = [Id, username, password, False]
            self.closingAction = "accountCreationSuccess"
            root.quit()