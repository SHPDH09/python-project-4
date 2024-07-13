import tkinter as tk
import smtplib
from tkinter import messagebox

class MailApp:
    def __init__(self, master):
        self.master = master
        master.title("Mail Application")
        master.config(background="black")

        fields = [("From:", "from"), ("E-Mail Password:", "pass", "*"), ("To:", "to"), ("Subject:", "subject")]
        self.entries = {}
        
        for i, (label, key, *args) in enumerate(fields):
            tk.Label(master, text=label, background="black", foreground="green").grid(row=i, column=0, sticky="w", padx=5)
            entry = tk.Entry(master, width=50, show=args[0] if args else "", background="black", foreground="green",
                             highlightbackground="green", highlightcolor="green", highlightthickness=1)
            entry.grid(row=i, column=1, sticky="w", pady=10)
            self.entries[key] = entry
        
        tk.Label(master, text="Message:", background="black", foreground="green").grid(row=4, column=0, sticky="w", padx=5)
        self.body_text = tk.Text(master, height=6, width=50, background="black", foreground="green",
                                 highlightbackground="green", highlightcolor="green", highlightthickness=1)
        self.body_text.grid(row=4, column=1, sticky="w", pady=20)

        tk.Button(master, text="Send", command=self.send_mail, width=16, background="green", foreground="black", font=8).grid(row=5, column=0, columnspan=2, padx=200)

    def send_mail(self):
        try:
            data = {k: v.get() for k, v in self.entries.items()}
            data["body"] = self.body_text.get("1.0", tk.END)
            
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(data["from"], data["pass"])

            message = f"Subject: {data['subject']}\n\n{data['body']}"
            server.sendmail(data["from"], data["to"], message)
            server.quit()
            
            messagebox.showinfo("Success", "Email sent successfully!")
            
            # Clear input fields
            for entry in self.entries.values():
                entry.delete(0, tk.END)
            self.body_text.delete("1.0", tk.END)

        except Exception as e:
            messagebox.showerror("Error", str(e))

root = tk.Tk()
app = MailApp(root)
root.geometry("550x350")
root.mainloop()
