import sqlite3
import tkinter as tk
class editChildren():
    def __init__(self,root,childID):
        for child in root.winfo_children():
            child.destroy()
        root.title("Login")
        root.geometry("400x300")
        self.childID = childID
        self.closingAction = "quit"
    
    def main(self, root):
        with sqlite3.connect('Details.db') as conn:
            print(self.childID)
            cursor = conn.cursor()
            sql = "SELECT Username, Password FROM main.ChildAccountDetails WHERE AccountID=?"
            cursor.execute(sql,(self.childID,))
            result = cursor.fetchall()
            if result != []:
                username = result[0][0]
                password = result[0][1]
                username_entry = tk.Entry(root)
                username_entry.insert(0,username)
                username_entry.pack()
                password_entry = tk.Entry(root, show="*")
                password_entry.insert(0,password)
                password_entry.pack()
                submit_button = tk.Button(root, text="update child details", command=lambda: self.submit(root, username_entry, password_entry), width=20)
                submit_button.pack()
                root.mainloop()
                return(self.closingAction)
    
    def submit(self, root, username_entry, password_entry):
        username = username_entry.get()
        password = password_entry.get()
        print(username)
        print(password)

        with sqlite3.connect('Details.db') as conn:
            cursor = conn.cursor()
            sql = '''UPDATE main.ChildAccountDetails SET Username=?, Password=? WHERE AccountID=? '''
            cursor.execute(sql, (username,password,self.childID))
            self.closingAction = "childEditSuccess"
            root.quit()
    