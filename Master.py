#"master" file which acts as a controller for the app
#imports each page as its own distinct module so that variables can be exchanged between files
#(necessary for tracking user details)
import tkinter as tk
import sqlite3
import App_Login
root = tk.Tk()
loginPage = App_Login.loginPage(root)
loginResponse = loginPage.main(root)
userDetails = loginResponse[0]
closingAction = loginResponse[1]
print(userDetails)
print(closingAction)