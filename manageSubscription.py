import tkinter as tk
import sqlite3
import hashlib
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
            currentTier = tk.StringVar(mainContainer)
            tierSelection = tk.OptionMenu(mainContainer, currentTier, *subscriptionTiers)
            tierSelection.pack()
            changeTierButton = tk.Button(mainContainer, text = "change tier", command=lambda: self.changeTier(userDetails,currentTier),width=10)
            changeTierButton.pack()
            cardDetails = tk.LabelFrame(mainContainer, text="payment details:")
            cardDetails.pack(padx=10, pady=10)
            cardNoEntry = tk.Entry(cardDetails)
            expiryDateEntry = tk.Entry(cardDetails)
            securityCodeEntry = tk.Entry(cardDetails)
            cardNoEntry.pack()
            expiryDateEntry.pack()
            securityCodeEntry.pack()
            updateCardButton = tk.Button(mainContainer, text = "update payment details", command=lambda: self.updateCard(userDetails,cardNoEntry,expiryDateEntry,securityCodeEntry),width=15)
            updateCardButton.pack()
            self.root.mainloop()
            return self.closing_action
    
    def changeTier(self,userDetails,subscriptionTier):
        with sqlite3.connect('Details.db') as conn:
            newTier = subscriptionTier.get()
            cur = conn.cursor()
            sql = '''UPDATE AccountDetails SET subscriptionTier=? WHERE AccountID=?'''
            cur.execute(sql,(newTier,userDetails[0],))
            self.closing_action = "tierUpdateSuccess"
            self.root.quit()
    
    def updateCard(self,userDetails,cardNoEntry,expiryDateEntry,securityCodeEntry):
        cardNo = hashlib.new('sha256')
        cardNo.update(cardNoEntry.get().encode('utf-8'))
        cardNo.update(userDetails[0].encode('utf-8'))
        expiryDate = hashlib.new('sha256')
        expiryDate.update(expiryDateEntry.get().encode('utf-8'))
        expiryDate.update(userDetails[0].encode('utf-8'))
        securityCode = hashlib.new('sha256')
        securityCode.update(securityCodeEntry.get().encode('utf-8'))
        securityCode.update(userDetails[0].encode('utf-8'))
        with sqlite3.connect('Details.db') as conn:
            cur = conn.cursor()
            sql = '''UPDATE AccountDetails SET CardNo=?,ExpiryDate=?,SecurityCode=? WHERE AccountID=?'''
            cur.execute(sql,(cardNo.hexdigest(),expiryDate.hexdigest(),securityCode.hexdigest(),userDetails[0]))
            self.closing_action = "paymentDetailsUpdateSuccess"
            self.root.quit()