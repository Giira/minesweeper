from tkinter import *
from tkinter import ttk
from grid import Grid

DIFFICULTY = ""

root = Tk()
root.title("Minesweeper")

ttk.Entry(root).grid()   # something to interact with


def dismiss():
    level_select.grab_release()
    level_select.destroy()


def choice_dismiss(choice):
    global DIFFICULTY 
    DIFFICULTY = choice
    dismiss()
    

level_select = Toplevel(root)
ls_frame = ttk.Frame(level_select, padding="5 5 5 5")
ls_frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(ls_frame, text="Choose your difficulty:").grid(column=0, row=0, sticky=N)
ttk.Button(level_select, text="Easy", command=lambda: choice_dismiss("Easy")).grid(column=1, row=0)
ttk.Button(level_select, text="Medium", command=lambda: choice_dismiss("Medium")).grid(column=2, row=0)
ttk.Button(level_select, text="Hard", command=lambda: choice_dismiss("Hard")).grid(column=3, row=0)

level_select.protocol("WM_DELETE_WINDOW", dismiss) # intercept close button
level_select.transient(root)   # dialog window is related to main
level_select.wait_visibility() # can't grab until window appears, so we wait
level_select.grab_set()        # ensure all input goes to our window
level_select.wait_window()     # block until window is destroyed


mainframe = ttk.Frame(root, padding="5 5")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()
