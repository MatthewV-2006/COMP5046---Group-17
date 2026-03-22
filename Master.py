#"master" file which acts as a controller for the app
#imports each page as its own distinct module so that variables can be exchanged between files
#(necessary for tracking user details)
import tkinter as tk
import sqlite3
import App_Login
import home
import contactDetails
import childCreation
root = tk.Tk()
loginPage = App_Login.loginPage(root)
loginResponse = loginPage.main(root)
userDetails = loginResponse[0]
closingAction = loginResponse[1]
#print(userDetails)
#print(closingAction)
if closingAction == "signInSuccess" or closingAction == "accountCreationSuccess":
    homePage = home.home(root)
    closingAction = homePage.main(root,userDetails)
    if closingAction == "updateDetails":
        updateDetails = contactDetails.contactDetails(root, userDetails)
        updateResponse = updateDetails.main(root)
        userDetails = updateResponse[0]
        closingAction = updateResponse[1]
    elif closingAction == "createChildAccount":
        childCreation = childCreation.childCreation(root, userDetails)
        childCreationResponse = childCreation.main(root)