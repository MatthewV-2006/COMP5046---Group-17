#"master" file which acts as a controller for the app
#imports each page as its own distinct module so that variables can be exchanged between files
#(necessary for tracking user details)
import tkinter as tk
import sqlite3
import App_Login
import contactDetails
import childCreation
import editChildren
import AccountMainPage
root = tk.Tk()
loginPage = App_Login.loginPage(root)
loginResponse = loginPage.main(root)
userDetails = loginResponse[0]
closingAction = loginResponse[1]
if closingAction == "signInSuccess" or closingAction == "accountCreationSuccess":
    homePage = AccountMainPage.home(root)
    homePageResponse = homePage.main(root,userDetails)
    if homePageResponse[0] == "updateDetails":
        updateDetails = contactDetails.contactDetails(root, userDetails)
        updateResponse = updateDetails.main(root)
        userDetails = updateResponse[0]
        closingAction = updateResponse[1]

    elif homePageResponse[0] == "createChildAccount":
        childCreation = childCreation.childCreation(root, userDetails)
        childCreationResponse = childCreation.main(root)
    
    elif homePageResponse[0] == "editChildAccount":
        editChildren = editChildren.editChildren(root, homePageResponse[1])
        editChildrenResponse = editChildren.main(root)

    elif homePageResponse[0] == "addMedication":
        MedicationPage = AccountMainPage.home(root)
        closingAction = MedicationPage.main(root, userDetails)