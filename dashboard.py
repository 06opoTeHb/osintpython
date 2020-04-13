#osint project dashboard
#Developed by Matt Hofmann, Simeon Wilson, and Zachary Fleck
import tkinter as tk

#initialize frame
win = tk.Tk()
win.title("OSINT Dashboard")
win.geometry('300x300')
#make window not resizable
win.resizable(0,0)
#label
label1 = tk.Label(win, text="Please select a site").grid(column=1, row=1)
#reddit button
action = tk.Button(win, text="Reddit", bg='#FF4301', activebackground='#FF4301')
action.grid(column=1, row=2)
action.config(height='4', width='20')
#twitter button
action2 = tk.Button(win, text="Twitter", bg='#00acee', activebackground='#00acee')
action2.grid(column=2, row=2)
action2.config(height='4', width='20')

#show gui
win.mainloop()