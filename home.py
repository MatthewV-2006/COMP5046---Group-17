import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from medicationsDB import get_med_db
from add_medication import open_add_med

# home page
import sqlite3
class home:
    def __init__(self, root):
        #removes tkinter elements from previous page
        for child in root.winfo_children():
            child.destroy()

        self.root = root
        self.closing_action = "quit"
        self.total_num_medication = 3
        self.taken_meds = 0
        self.medication_reminders = []
        
        # sets the title of the window
        root.title("Home page")
        
        # sets the size of the window
        root.geometry("850x850")

    # sorts reminders and retrieves the latest due medication
    def get_due_medication(self):
        now = datetime.now()
        medications = []
        for name_of_med, reminder_time in self.medication_reminders:
            reminder_time = datetime.strptime(reminder_time, "%H:%M")
            reminder_time = reminder_time.replace(year=now.year, month=now.month, day=now.day)
            medications.append((name_of_med, reminder_time))
            
        medications.sort(key=lambda x: x[1])

        for name_of_med, reminder_time in medications:
            if reminder_time >= now:
                return name_of_med, reminder_time.strftime("%H:%M")
            
        if medications:
            return medications[0][0], medications[0][1].strftime("%H:%M")

        return None, None

    def load_medications(self, listbox):
        rows = get_med_db()
        for name, dose, reminder_time in rows:
            listbox.insert(tk.END, f"{reminder_time} - {name}")
            self.medication_reminders.append((name, reminder_time))
    
    # update contact details 
    def update_details(self, root):
        self.closing_action = "updateDetails"
        root.quit()

    # adds medication
    def add_medication(self):
        open_add_med(self.root, self.schedule_list, self.medication_reminders)

    # updates medication
    def modify_medication(self):
        print("Modify medication clicked")

    # set reminder for medication
    def set_medication_reminder(self):
        print("Set reminder clicked")
    
    # view medication history
    def view_history(self):
        print("View history clicked")

    # changes the label text when the 'Mark as Taken' button is clicked
    def taken_medication(self, progress_bar, label, status_label):
        self.taken_meds += 1
        progress_bar["value"] = self.taken_meds
        label.config(text=f"{self.taken_meds} / {self.total_num_medication} medications taken")
        status_label.config(text="Medication Taken")

    def main(self, root, userDetails):
        # main container frame
        main_container = ttk.Frame(root)
        main_container.pack(fill="both", expand=True)
        
        # canvas to display everything
        canvas = tk.Canvas(main_container)
        canvas.pack(side="left", fill = "both", expand = True)

        #creates a scrollbar for navigating the window
        scrollbar = ttk.Scrollbar(main_container, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        frame = ttk.Frame(canvas)
        canvas_window = canvas.create_window((0, 0), window=frame, anchor="nw")

        canvas.bind("<Configure>", lambda e: canvas.itemconfig(canvas_window, width=e.width))
        frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        #button for updating the details of a user account
        update_details_button = ttk.Button(frame, text="Update Contact Details", command=lambda: self.update_details(root)).pack()

        # main frame
        overview_frame = ttk.LabelFrame(frame, text="Today's Medication Overview", padding=20)
        overview_frame.pack(padx=20, pady=20, fill="x")

        status_label = ttk.Label(overview_frame, text="")
        status_label.pack()
        
        # Today's medication schedule
        schedule_frame = ttk.LabelFrame(frame, text="Today's Schedule", padding=10)
        schedule_frame.pack(padx=20, pady=10, fill="both")

        self.schedule_list = tk.Listbox(schedule_frame)
        self.schedule_list.pack(fill="both")

        self.load_medications(self.schedule_list)
        
        med_name, reminder_time = self.get_due_medication()
        
        if med_name and reminder_time:
            name_label = ttk.Label(overview_frame, text=f"Medication: {med_name}")
            name_label.pack(fill = "x", padx = 10)
            time_label = ttk.Label(overview_frame, text=f"Take at: {reminder_time}")
            time_label.pack(fill = "x", padx = 10)
        else:
            name_label = ttk.Label(overview_frame, text=f"Medication: None")
            name_label.pack(fill = "x", padx = 10)
            time_label = ttk.Label(overview_frame, text=f"Take at: --")
            time_label.pack(fill = "x", padx = 10)

        options_frame = ttk.LabelFrame(frame, text="Medication Options", padding=10)
        options_frame.pack(padx=20, pady=20, fill="x")

        # Medication options
        ttk.Button(options_frame, text="Add Medication", command=self.add_medication).pack(fill="x")
        ttk.Button(options_frame, text="Edit Medication", command=self.modify_medication).pack(fill="x")
        ttk.Button(options_frame, text="Set Reminder", command=self.set_medication_reminder).pack(fill="x")
        ttk.Button(options_frame, text="View History", command=self.view_history).pack(fill="x")

        progress_frame = ttk.LabelFrame(frame, text="Progress", padding=10)
        progress_frame.pack(padx=20, pady=20, fill="x")

        progress_label = ttk.Label(progress_frame, text=f"{self.taken_meds} / {self.total_num_medication} medications taken")
        progress_label.pack()

        """creates progress bar which becomes full when number of medication taken is equal
        to total number of medications so the user can track their progress 
        """
        progress_bar = ttk.Progressbar(progress_frame, maximum=self.total_num_medication)
        progress_bar.pack(fill="x")

        # Button to click if you have taken your next due medication
        ttk.Button(overview_frame, text="Mark as Taken", command=lambda: self.taken_medication(progress_bar, progress_label, status_label)).pack()

        # displays details of users if the user has admin
        if userDetails[3]:
            #creates new section for user accounts
            users = ttk.LabelFrame(frame, text="Users", padding=10)
            users.pack(padx=20, pady=20, fill="x")

            user_list = tk.Listbox(users)
            user_list.pack(fill="both")

            #retrieves details of existing users
            sql = "SELECT AccountID, username, isAdmin FROM AccountDetails"
            with sqlite3.connect('Details.db') as conn:
                cur = conn.cursor()
                cur.execute(sql,)
                for row in cur.fetchall():
                    user_list.insert(tk.END, str(row))

        return self.closing_action
    
if __name__ == "__main__":
    # creates main window
    root = tk.Tk()
    
    # user test data
    userDetails = ("id", "username", "email", True)

    # creates app instance
    app = home(root)
    
    # creates user interface for home page
    app.main(root, userDetails)
    
    # starts the program and keeps the window open
    root.mainloop()