from tkinter import *
from ui import build_gui
from db import create_table

root = Tk()
root.title("Course Organizer")
root.geometry("650x400")
root.configure(bg="lightblue")  # Change background color here

create_table()
build_gui(root)

root.mainloop()
