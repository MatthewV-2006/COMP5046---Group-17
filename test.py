import tkinter as tk
import sqlite3
import App_Login
import home
import contactDetails
import AccountMainPage
root = tk.Tk()

#for testing new features without having to run the whole program

loginPage = AccountMainPage.home(root)
loginResponse = loginPage.main(root, ['0', 'Admin', 'Admin1234', 1, 'gschlecurity@aweso.me', '+1337 6769 420'])
