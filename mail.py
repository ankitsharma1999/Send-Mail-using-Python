import smtplib
import config
import tkinter as tk
from tkinter import ttk
import sys

main = tk.Tk()

main.geometry("400x250")
main.title("Send Mail")
main.resizable(False, False)

def popupmsg(msg):

    popup = tk.Tk()
    popup.wm_title("Warning")
    popup.resizable(False, False)
    popup.geometry("200x100")

    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", bg="red", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def send_mail():
    while True:
        msg=str(entry1.get())
        if msg=="":
            popupmsg("Message Field is Empty")
        else:
            break
    while True:
        recv=str(entry2.get())
        if recv=="":
            popupmsg("Enter Reciever Mail Id")
        else:
            break
    while True:
        pin=str(entry3.get())
        if pin=="":
            popupmsg("Please Enter The Pin")
        else:
            break
    if pin==config.Pin:
        pass
    else:
        popupmsg("Wrong Pin")
        sys.exit()
    try:
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(config.Email, config.Password)
        server.sendmail(config.Email, recv, msg)
        server.quit()
        popupmsg("Email Sent!")
    except:
        popupmsg("Email Not Sent.\n Some Error Occured")
    sys.exit()


entry1=tk.Entry()
entry1.focus_set()
entry1.grid(column=1, row=0)

p_label1 = tk.Label(text="Enter your message here")
p_label1.grid(column=0, row=0)

p_label2 = tk.Label(text="Enter the Mail Id of Reciever")
p_label2.grid(column=0,row=1)

p_label3 = tk.Label(text="Confirm Your Pin")
p_label3.grid(column=0, row=2)

entry2 = tk.Entry()
entry2.grid(column=1, row=1)

entry3 = tk.Entry(show="*")
entry3.grid(column=1, row=2)

btn = tk.Button(text="Send", bg='green', command = send_mail)
btn.grid(column=1,row=3)

main.mainloop()
