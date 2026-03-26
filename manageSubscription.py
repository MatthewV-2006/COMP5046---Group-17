import tkinter as tk
import sqlite3
class manageSubscription:
    def __init__(self,root):
        for child in root.winfo_children():
            child.destroy()

        self.root = root
        self.closing_action = None
        root.title = "Manage subscriptions"
        root.geometry = ("400x300")
    
    def main(self,userDetails):
        mainContainer = tk.Frame(self.root)
        mainContainer.pack(fill="both",expand=True)
        currentTier = tk.Text(mainContainer, height=5)
        currentTier.insert(tk.END, "Current subscription tier: ")
        with sqlite3.connect('Details.db') as conn:
            cur = conn.cursor()
            sql = '''SELECT subscriptionTier FROM AccountDetails WHERE AccountID=?'''
            cur.execute(sql,(userDetails[0],))
            result = cur.fetchone()
            currentTier.insert(tk.END, result)
            currentTier.pack()
            subscriptionTiers = ["None","Family","Limitless"]
            tierSelection = tk.OptionMenu(mainContainer, "None", *subscriptionTiers)
            tierSelection.pack()
            cardDetails = tk.LabelFrame(mainContainer, text="payment details:", padding = 10)
            cardDetails.pack()
            cardNoEntry = tk.Entry(cardDetails)
            expiryDateEntry = tk.Entry(cardDetails)
            securityCodeEntry = tk.Entry(cardDetails)
            cardNoEntry.pack()
            expiryDateEntry.pack()
            securityCodeEntry.pack()