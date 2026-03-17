# importing home page
import home
import tkinter as tk

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
    
    # closes login window and opens the home page window
    if username and password:
        root.destroy()
        home.open_home_page()

root = tk.Tk()
root.title("Login")
root.geometry("400x300")

login_button = tk.Button(root, text="Login", command=login, width=10)
login_button.pack()

username_entry = tk.Entry(root)
password_entry = tk.Entry(root, show="*")

submit_button = tk.Button(root, text="Submit", command=submit, width=10)
root.mainloop()
