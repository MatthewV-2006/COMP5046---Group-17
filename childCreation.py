import tkinter as tk
import sqlite3

class contactDetails:
    def __init__(self,root,userDetails):
        for child in root.winfo_children():
            child.destroy()
        root.title("Login")
        root.geometry("400x300")
        self.userDetails = userDetails
        self.closingAction = "quit"
    
    def main(self, root):
        username_entry = tk.Entry(root)
        username_entry.pack()
        password_entry = tk.Entry(root, show="*")
        password_entry.pack()
        submit_button = tk.Button(root, text="create child account", command=lambda: self.submit(root, username_entry, password_entry), width=10)
        submit_button.pack()
        root.mainloop()
        return(self.userDetails,self.closingAction)
    
    def submit(self, root, username_entry, password_entry):
        username = username_entry.get()
        password = password_entry.get()
        print(self.userDetails[0])
        print(username)
        print(password)
        sql = ""

        with sqlite3.connect('Details.db') as conn:
            cursor = conn.cursor()