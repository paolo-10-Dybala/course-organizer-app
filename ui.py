from tkinter import *
from db import add_course, delete_course
from search import search_course

def build_gui(root):
    Label(root, text="Course Name").grid(row=0, column=0)
    name_entry = Entry(root)
    name_entry.grid(row=0, column=1)

    Label(root, text="Instructor").grid(row=1, column=0)
    instructor_entry = Entry(root)
    instructor_entry.grid(row=1, column=1)

    Label(root, text="Semester").grid(row=2, column=0)
    semester_entry = Entry(root)
    semester_entry.grid(row=2, column=1)

    results = Listbox(root, width=60)
    results.grid(row=5, columnspan=3)

    def handle_add():
        add_course(name_entry.get(), instructor_entry.get(), semester_entry.get())
        results.insert(END, f"Added: {name_entry.get()}")

    def handle_delete():
        delete_course(name_entry.get())
        results.insert(END, f"Deleted: {name_entry.get()}")

 def handle_search():
    results.delete(0, END)
    query = name_entry.get().strip()  # Use course name field for search
    if query == "":
        results.insert(END, "Please enter course or instructor name to search.")
        return
    matches = search_course(query)
    if not matches:
        results.insert(END, "No results found.")
    for m in matches:
        results.insert(END, f"{m[0]} - {m[1]} ({m[2]})")

    Button(root, text="Add Course", command=handle_add).grid(row=3, column=0)
    Button(root, text="Delete Course", command=handle_delete).grid(row=3, column=1)
    Button(root, text="Search Course", command=handle_search).grid(row=3, column=2)