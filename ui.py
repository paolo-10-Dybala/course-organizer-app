from tkinter import *
from db import add_course, delete_course
from search import search_course

root = Tk()
root.title("Course Management System")
root.configure(bg="#f0f2f5")
root.state('zoomed')  # Open in full screen on Windows

Label(root, text="Course Name", bg="#f0f2f5", font=("Arial", 10, "bold")).grid(row=0, column=0, pady=5, padx=10, sticky=W)
name_entry = Entry(root, font=("Arial", 10))
name_entry.grid(row=0, column=1, pady=5, padx=10)

Label(root, text="Instructor", bg="#f0f2f5", font=("Arial", 10, "bold")).grid(row=1, column=0, pady=5, padx=10, sticky=W)
instructor_entry = Entry(root, font=("Arial", 10))
instructor_entry.grid(row=1, column=1, pady=5, padx=10)

Label(root, text="Semester", bg="#f0f2f5", font=("Arial", 10, "bold")).grid(row=2, column=0, pady=5, padx=10, sticky=W)
semester_entry = Entry(root, font=("Arial", 10))
semester_entry.grid(row=2, column=1, pady=5, padx=10)

results = Listbox(root, width=100, font=("Courier", 10), bg="white")
results.grid(row=5, column=0, columnspan=3, pady=10, padx=10)

def handle_add():
    add_course(name_entry.get(), instructor_entry.get(), semester_entry.get())
    results.insert(END, f"Added: {name_entry.get()}")

def handle_delete():
    delete_course(name_entry.get())
    results.insert(END, f"Deleted: {name_entry.get()}")

def handle_search():
    results.delete(0, END)
    query = name_entry.get().strip()
    if query == "":
        results.insert(END, "Please enter course or instructor name to search.")
        return
    matches = search_course(query)
    if not matches:
        results.insert(END, "No results found.")
    for m in matches:
        results.insert(END, f"{m[0]} - {m[1]} ({m[2]})")

Button(root, text="Add Course", command=handle_add, bg="#4CAF50", fg="white", font=("Arial", 9, "bold"), width=20).grid(row=3, column=0, pady=10)
Button(root, text="Delete Course", command=handle_delete, bg="#f44336", fg="white", font=("Arial", 9, "bold"), width=20).grid(row=3, column=1, pady=10)
Button(root, text="Search Course", command=handle_search, bg="#2196F3", fg="white", font=("Arial", 9, "bold"), width=20).grid(row=3, column=2, pady=10)

root.mainloop()

