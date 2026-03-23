import tkinter as tk
from tkinter import ttk
from datetime import datetime
import sqlite3
from add_medication import open_add_med
class home:
    def __init__(self, root):
        #removes tkinter elements from previous page
        for child in root.winfo_children():
            child.destroy()

        self.root = root
        self.closing_action = None
        self.medication_reminders = []
        self.closing_message = "quit"
        self.total_num_medication = 3
        self.taken_meds = 0

        # sets the title of the window
        root.title("Home page")

        # sets the size of the window
        root.geometry("850x850")


        # example medication data

    # update contact details
    def update_details(self,root):
        self.closing_action = "updateDetails"
        root.quit()


    
    def main(self,root,userDetails):
        main_container = ttk.Frame(root)
        main_container.pack(fill = "both", expand = True)        
        
        # canvas to display everything
        canvas = tk.Canvas(main_container)
        canvas.pack(side = "left", fill = "both", expand = True)
        
        scroll_bar = ttk.Scrollbar(main_container, orient = "vertical", command = canvas.yview)
        scroll_bar.pack(side = "right", fill = "y")
        canvas.configure(yscrollcommand=scroll_bar.set)

        scrollable_frame = ttk.Frame(canvas)
        scrollable_window = canvas.create_window((0,0), window=scrollable_frame, anchor = "nw")

        def on_canvas_configure(event):
            canvas.itemconfig(scrollable_window, width = event.width)
        
        canvas.bind("<Configure>", on_canvas_configure)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        scrollable_frame.columnconfigure(0, weight = 1)

                        
        #button for updating the details of a user account
        update_details_button = ttk.Button(scrollable_frame, text = "Update contact details", command=lambda: self.update_details(root))
        update_details_button.pack(pady = 10)




        # displays details of users if the user has admin
        if userDetails[3]:
            #creates new section for user accounts
            users = ttk.LabelFrame(scrollable_frame, text = "Users:", padding=10)
            users.columnconfigure(0, weight = 1)
            users.pack(padx=20, pady=20, fill="both",expand=True)
            user_list = tk.Listbox(users)
            user_list.pack(fill = "both", expand = True)

            #retrieves details of existing users
            sql = "SELECT AccountID, username, isAdmin FROM AccountDetails"
            with sqlite3.connect('Details.db') as conn:
                cur = conn.cursor()
                cur.execute(sql,)
                iterator = cur.fetchall()
                for row in iterator:
                    print(row)
                    user_list.insert(tk.END, str(row))

        # starts the program and keeps the window open
        scrollable_frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))
        root.mainloop()
        return(self.closing_action)