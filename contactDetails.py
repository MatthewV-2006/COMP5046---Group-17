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
        email_entry = tk.Entry(root)
        email_entry.pack()
        phone_entry = tk.Entry(root)
        phone_entry.pack()
        submit_button = tk.Button(root, text="update details", command=lambda: self.submit(root, email_entry, phone_entry), width=10)
        submit_button.pack()
        root.mainloop()
        return(self.userDetails,self.closingAction)
    
    def submit(self, root, email_entry, phone_entry):
        email = email_entry.get()
        phone = phone_entry.get()
        sql = "UPDATE AccountDetails SET email=?, phone=? WHERE AccountID=?"

        with sqlite3.connect('Details.db') as conn:
            cursor = conn.cursor()
            cursor.execute(sql,(email,phone,self.userDetails[0]))
            sql = "SELECT email,phone FROM AccountDetails WHERE AccountID=?"
            cursor.execute(sql,(self.userDetails[0],))
            row = cursor.fetchall()
            self.userDetails[4] = row[0]
            self.userDetails[5] = row[5]
            self.closingAction = "updateSuccess"
            root.quit()
            conn.close()