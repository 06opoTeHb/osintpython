# osint project dashboard
# Developed by Matt Hofmann, Simeon Wilson, and Zachary Fleck
import tkinter as tk

# initialize frame
win = tk.Tk()
win.title("OSINT Dashboard")
win.geometry('300x350')
# make window not resizable
win.resizable(0, 0)
rv = tk.IntVar()
tv = tk.IntVar()


#reddit fields assigned to variables outside of reddittext() method
r1 = tk.Label(win, text="Search")
r2 = tk.Label(win, text="Subreddit")
r3 = tk.Label(win, text="")
r4 = tk.Label(win, text="Sort results by")
r5 = tk.Radiobutton(win, text="Hot", variable=rv, value=1, command=rv.set(1))
r6 = tk.Radiobutton(win, text="New", variable=rv, value=2, command=rv.set(2))
r7 = tk.Radiobutton(win, text="Top", variable=rv, value=3, command=rv.set(3))
r8 = tk.Radiobutton(win, text="Controversial", variable=rv, value=4, command=rv.set(4))
r9 = tk.Radiobutton(win, text="Rising", variable=rv, value=5, command=rv.set(5))
e1 = tk.Entry(win)
e2 = tk.Entry(win)
submitreddit = tk.Button(win, text="Submit")


# reddit text entry field
def reddittext():
    #removes twitter residue
    t1.grid_forget()
    t2.grid_forget()
    t3.grid_forget()
    t4.grid_forget()
    t5.grid_forget()
    e1.grid_forget()
    submittwit.grid_forget()
    # places reddit fields on the window
    r1.grid(row=3, column=1)
    r2.grid(row=4, column=1)
    r3.grid(row=5, column=1)
    r4.grid(row=6, column=1)
    r5.grid(row=7, column=1)
    r6.grid(row=8, column=1)
    r7.grid(row=9, column=1)
    r8.grid(row=10, column=1)
    r9.grid(row=11, column=1)
    e1.grid(row=3, column=2)
    e2.grid(row=4, column=2)
    submitreddit.grid(row=12, column=2)


#twitter fields assigned to variables outside of twittertext() method
t1 = tk.Label(win, text="Search")
te1 = tk.Entry(win)
t2 = tk.Label(win, text="")
t5 = tk.Label(win, text="Sort results by")
t3 = tk.Radiobutton(win, text="New", variable=tv, value=1, command=tv.set(1))
t4 = tk.Radiobutton(win, text="Top", variable=tv, value=2, command=tv.set(2))
submittwit = tk.Button(win, text="Submit")


# twitter text entry field
def twittertext():
    # removes reddit residue
    r1.grid_forget()
    r2.grid_forget()
    r3.grid_forget()
    r4.grid_forget()
    r5.grid_forget()
    r6.grid_forget()
    r7.grid_forget()
    r9.grid_forget()
    r8.grid_forget()
    e1.grid_forget()
    e2.grid_forget()
    submitreddit.grid_forget()
    #places twitter fields on the window
    t1.grid(row=3, column=1)
    te1.grid(row=3, column=2)
    t2.grid(row=4, column=1)
    t5.grid(row=5, column=1)
    t3.grid(row=6, column=1)
    t4.grid(row=7, column=1)
    submittwit.grid(row=7, column=2)


# label
label1 = tk.Label(win, text="Please select a site").grid(column=1, row=1)
# reddit button
action = tk.Button(win, text="Reddit", bg='#FF4301', activebackground='#FF4301', command=reddittext)
action.grid(column=1, row=2)
action.config(height='4', width='20')
# twitter button
action2 = tk.Button(win, text="Twitter", bg='#00acee', activebackground='#00acee', command=twittertext)
action2.grid(column=2, row=2)
action2.config(height='4', width='20')

# show gui
win.mainloop()
