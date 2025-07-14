import sqlite3

def connect():
    return sqlite3.connect("courses.db")

def create_table():
    conn = connect()
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS courses (name TEXT, instructor TEXT, semester TEXT)")
    conn.commit()
    conn.close()

def add_course(name, instructor, semester):
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO courses VALUES (?, ?, ?)", (name, instructor, semester))
    conn.commit()
    conn.close()

def delete_course(name):
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM courses WHERE name = ?", (name,))
    conn.commit()
    conn.close()

def get_all_courses():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM courses")
    data = c.fetchall()
    conn.close()
    return data
