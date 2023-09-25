import smtplib
import tkinter as tk
from tkinter import messagebox

class MailApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mail App")

        # Create GUI elements
        self.sender_label = tk.Label(self.root, text="Sender:")
        self.sender_entry = tk.Entry(self.root)
        self.receiver_label = tk.Label(self.root, text="Receiver:")
        self.receiver_entry = tk.Entry(self.root)
        self.subject_label = tk.Label(self.root, text="Subject:")
        self.subject_entry = tk.Entry(self.root)
        self.body_label = tk.Label(self.root, text="Body:")
        self.body_text = tk.Text(self.root, height=10, width=50)
        self.send_button = tk.Button(self.root, text="Send", command=self.send_email)

        # Place GUI elements on the window
        self.sender_label.grid(row=0, column=0)
        self.sender_entry.grid(row=0, column=1)
        self.receiver_label.grid(row=1, column=0)
        self.receiver_entry.grid(row=1, column=1)
        self.subject_label.grid(row=2, column=0)
        self.subject_entry.grid(row=2, column=1)
        self.body_label.grid(row=3, column=0)
        self.body_text.grid(row=3, column=1)
        self.send_button.grid(row=4, column=1)

        # Start the mainloop
        self.root.mainloop()

    def send_email(self):
        # Get the email details from the GUI
        sender = self.sender_entry.get()
        receiver = self.receiver_entry.get()
        subject = self.subject_entry.get()
        body = self.body_text.get("1.0", "end-1c")

        # Create an SMTP object
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()

        # Login to the SMTP server using an app password
        smtp_server.login(sender, "YOUR_APP_PASSWORD")

        # Send the email
        smtp_server.sendmail(sender, receiver, f"Subject: {subject}\n\n{body}")

        # Close the SMTP connection
        smtp_server.quit()

        # Show a success message
        messagebox.showinfo("Success", "Email sent successfully!")

if __name__ == "__main__":
    mail_app = MailApp()