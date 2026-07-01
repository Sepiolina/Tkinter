import tkinter as tk
from tkinter import messagebox
import random

class VintageOfficeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OmniCorp Workstation v1.04")
        self.root.geometry("800x600")
        self.root.configure(bg="#d9d9d9")
        
        self.retro_font = ("MS Sans Serif", 10)
        self.retro_font_bold = ("MS Sans Serif", 10, "bold")
        self.terminal_font = ("Courier", 9)
        
        self.tasks_completed = 0
        self.corruption_level = 0
        
        self.widget_cfg = {"bg": "#d9d9d9", "fg": "black", "font": self.retro_font}
        self.btn_cfg = {"bg": "#d9d9d9", "fg": "black", "font": self.retro_font, "relief": "raised", "bd": 2, "activebackground": "#aeaeae"}
        
        self.setup_ui()
        self.glitch_loop()

    def setup_ui(self):
        self.menu_bar = tk.Frame(self.root, bg="#d9d9d9", bd=1, relief="raised")
        self.menu_bar.pack(fill="x", side="top")
        
        for text in ["File", "Edit", "View", "Tools", "Help"]:
            btn = tk.Button(self.menu_bar, text=text, relief="flat", bg="#d9d9d9", font=self.retro_font, padx=5, pady=2)
            btn.pack(side="left")
            if text == "Help":
                btn.config(command=self.trigger_help_glitch)

        self.workspace = tk.Frame(self.root, bg="#808080", bd=2, relief="sunken")
        self.workspace.pack(fill="both", expand=True, padx=4, pady=4)

        self.sidebar = tk.Frame(self.workspace, bg="#d9d9d9", width=150, bd=2, relief="raised")
        self.sidebar.pack(side="left", fill="y", padx=2, pady=2)
        self.sidebar.pack_propagate(False)

        tk.Label(self.sidebar, text="Applications", font=self.retro_font_bold, bg="#d9d9d9", fg="#000080").pack(anchor="w", padx=5, pady=5)
        
        self.btn_db = tk.Button(self.sidebar, text="🗄️ DataEntry.exe", anchor="w", command=self.open_data_entry, **self.btn_cfg)
        self.btn_db.pack(fill="x", padx=4, pady=2)
        
        self.btn_mail = tk.Button(self.sidebar, text="✉️ IntraMail.exe", anchor="w", command=self.open_email, **self.btn_cfg)
        self.btn_mail.pack(fill="x", padx=4, pady=2)
        
        self.btn_logs = tk.Button(self.sidebar, text="📁 System_Logs", anchor="w", command=self.open_logs, **self.btn_cfg)
        self.btn_logs.pack(fill="x", padx=4, pady=2)

        self.main_window = tk.Frame(self.workspace, bg="#3b6ea5", bd=2, relief="sunken") # Classic Teal Desktop color
        self.main_window.pack(side="right", fill="both", expand=True, padx=2, pady=2)
        
        self.status_bar = tk.Frame(self.root, bg="#d9d9d9", bd=1, relief="raised")
        self.status_bar.pack(fill="x", side="bottom")
        
        self.status_text = tk.StringVar(value="System Ready. Quota: 0/1000")
        self.status_label = tk.Label(self.status_bar, textvariable=self.status_text, font=self.retro_font, bg="#d9d9d9", anchor="w")
        self.status_label.pack(side="left", fill="x", padx=5, pady=2)
        
        self.clock_label = tk.Label(self.status_bar, text="08:00 AM", font=self.retro_font, bg="#d9d9d9", bd=1, relief="sunken", padx=10)
        self.clock_label.pack(side="right", pady=2, padx=2)

        self.current_frame = None
        self.open_data_entry()

    def clear_main_window(self):
        if self.current_frame:
            self.current_frame.destroy()

    def create_window_frame(self, title):
        self.clear_main_window()
        
        win = tk.Frame(self.main_window, bg="#d9d9d9", bd=2, relief="raised")
        win.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.title_bar = tk.Frame(win, bg="#000080", bd=1, relief="raised")
        self.title_bar.pack(fill="x", side="top", padx=1, pady=1)
        
        self.title_label = tk.Label(self.title_bar, text=title, bg="#000080", fg="white", font=self.retro_font_bold)
        self.title_label.pack(side="left", padx=5)
        
        content = tk.Frame(win, bg="#d9d9d9", bd=2, relief="flat")
        content.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.current_frame = win
        return content

    def open_data_entry(self):
        body = self.create_window_frame("OmniCorp Data Ledger v1.2")
        
        tk.Label(body, text="Enter daily ledger values below. Do not leave fields blank.", **self.widget_cfg).pack(anchor="w", pady=5)
        
        form_frame = tk.Frame(body, bg="#d9d9d9")
        form_frame.pack(fill="x", pady=10)
        
        tk.Label(form_frame, text="Serial ID:", **self.widget_cfg).grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.ent_id = tk.Entry(form_frame, font=self.retro_font, bd=2, relief="sunken")
        self.ent_id.insert(0, str(random.randint(10000, 99999)))
        self.ent_id.grid(row=0, column=1, padx=5, pady=5)
        
        self.lbl_value_field = tk.Label(form_frame, text="Target Output:", **self.widget_cfg)
        self.lbl_value_field.grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.ent_val = tk.Entry(form_frame, font=self.retro_font, bd=2, relief="sunken")
        self.ent_val.grid(row=1, column=1, padx=5, pady=5)
        
        btn_sub = tk.Button(body, text="Commit Entry", command=self.submit_data, **self.btn_cfg)
        btn_sub.pack(pady=10)

    def submit_data(self):
        val = self.ent_val.get()
        if not val:
            return
            
        self.tasks_completed += 1
        self.status_text.set(f"System Ready. Quota: {self.tasks_completed * 45}/1000")
        
        if self.tasks_completed >= 3:
            self.corruption_level = 1
        if self.tasks_completed >= 6:
            self.corruption_level = 2
        if self.tasks_completed >= 9:
            self.corruption_level = 3

        if self.corruption_level == 1:
            self.ent_val.delete(0, tk.END)
            if random.random() > 0.4:
                self.ent_val.insert(0, "STILL HERE")
        elif self.corruption_level == 2:
            self.lbl_value_field.config(text="Is anyone there?:")
            self.ent_val.delete(0, tk.END)
            self.ent_val.insert(0, "IT BLINKS")
        elif self.corruption_level >= 3:
            self.lbl_value_field.config(text="⚠️ SYSTEM BREACH ⚠️", fg="red")
            self.ent_val.delete(0, tk.END)
            self.ent_val.insert(0, "LET ME OUT")
            
        if self.corruption_level < 2:
            self.ent_id.delete(0, tk.END)
            self.ent_id.insert(0, str(random.randint(10000, 99999)))
            if self.corruption_level == 0:
                self.ent_val.delete(0, tk.END)

    def open_email(self):
        body = self.create_window_frame("IntraMail - Inbox")
        
        mail_split = tk.PanedWindow(body, orient="vertical", bd=2, relief="sunken")
        mail_split.pack(fill="both", expand=True)
        
        list_frame = tk.Frame(mail_split, bg="#ffffff")
        preview_frame = tk.Frame(mail_split, bg="#ffffff", bd=2, relief="sunken")
        
        mail_split.add(list_frame, minsize=100)
        mail_split.add(preview_frame, minsize=150)
        
        self.mail_text = tk.Text(preview_frame, font=self.retro_font, wrap="word", bg="#ffffff", fg="black", bd=0)
        self.mail_text.pack(fill="both", expand=True, padx=5, pady=5)
        self.mail_text.insert("1.0", "Select a message to view content.")
        self.mail_text.config(state="disabled")

        emails = [
            ("HR Dept", "Welcome to OmniCorp!", "Welcome to your new cubicle. Remember: your desk assignment is permanent. Do not speak to the night shift technicians."),
        ]
        
        if self.corruption_level >= 1:
            emails.append(("Facilities", "RE: Flickering lights", "We have received your complaints about the lights turning off on Floor 4. There are currently no active employees registered on Floor 4 besides you. Please ignore."))
        if self.corruption_level >= 2:
            emails.append(("System Admin", "CRITICAL ERROR: Overlap", "Do not look directly at the window elements if they begin to drift. It is a visual artifact. We are structuralizing. Do not move from your seat."))
        if self.corruption_level >= 3:
            emails.append(("⚠️ UNKNOWN", "I see you", "The screen is a mirror. The gray frame is a cage. Turn around."))

        for sender, subject, content in emails:
            mail_btn = tk.Button(
                list_frame, 
                text=f"From: {sender}  |  Subj: {subject}", 
                anchor="w", 
                bg="#ffffff", 
                relief="groove", 
                bd=1,
                font=self.retro_font,
                command=lambda c=content: self.view_email(c)
            )
            mail_btn.pack(fill="x")

    def view_email(self, content):
        self.mail_text.config(state="normal")
        self.mail_text.delete("1.0", tk.END)
        self.mail_text.insert("1.0", content)
        self.mail_text.config(state="disabled")

    def open_logs(self):
        body = self.create_window_frame("Text Pad - System_Logs.txt")
        text_area = tk.Text(body, font=self.terminal_font, bg="#ffffff", fg="#004000", bd=2, relief="sunken")
        text_area.pack(fill="both", expand=True)
        
        base_logs = (
            "[08:00:02] Boot sequence initiated...\n"
            "[08:01:45] Syncing user matrix with Central Core...\n"
            "[08:15:22] Network heartbeat: STABLE\n"
        )
        
        if self.corruption_level == 1:
            base_logs += "[08:22:11] WARNING: Discrepancy detected in workspace sensory feedback.\n"
        elif self.corruption_level == 2:
            base_logs += "[08:22:11] WARNING: Discrepancy detected...\n"
            base_logs += "[08:34:01] ERR: Human mass detected outside operational parameters.\n"
            base_logs += "[08:35:12] Sub-routine 'BREATHE' failing to respond.\n"
        elif self.corruption_level >= 3:
            base_logs += "[SYSTEM FAILURE]\n"
            base_logs = base_logs.replace(" ", " ☠️ ")
            base_logs += "\nTHE OFFICE IS EMPTY. WHY ARE YOU TYPING?"

        text_area.insert("1.0", base_logs)
        text_area.config(state="disabled")

    def trigger_help_glitch(self):
        if self.corruption_level < 2:
            messagebox.showinfo("Help Centered", "OmniCorp OS Support:\nEnsure tasks are completed on time to secure your departure authorization.")
        else:
            self.root.title("THERE IS NO HELP")
            messagebox.showerror("Error 666", "No exit route mapped to this terminal.")

    def glitch_loop(self):
        if self.corruption_level == 1:
            if random.random() > 0.85:
                self.clock_label.config(text="--:--")
            else:
                self.clock_label.config(text="08:24 AM")
                
        elif self.corruption_level == 2:
            self.btn_db.config(text="🗄️ Feed_Me.exe")
            if random.random() > 0.7:
                self.status_text.set("It gets cold here at night.")
                
        elif self.corruption_level >= 3:
            self.btn_db.config(text="💀 ALONE.exe")
            self.btn_mail.config(text="🩸 WATCHING")
            self.root.config(bg="#1a0000")
            if random.random() > 0.5:
                self.status_text.set(random.choice([
                    "DON'T LOOK AT THE WINDOWS", 
                    "EFFICIENCY IS SUFFERING", 
                    "YOU CANNOT UNSUBMIT"
                ]))
        
        self.root.after(3000, self.glitch_loop)

if __name__ == "__main__":
    root = tk.Tk()
    app = VintageOfficeApp(root)
    root.mainloop()
