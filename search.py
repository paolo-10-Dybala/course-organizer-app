from db import connect
def search_course(name_query):
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM courses WHERE name LIKE ?", ('%' + name_query + '%',))
    results = c.fetchall()
    conn.close()
    return results