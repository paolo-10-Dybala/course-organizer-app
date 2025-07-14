from db import connect

def search_course(query):
    conn = connect()
    c = conn.cursor()
    c.execute("""
        SELECT * FROM courses 
        WHERE name LIKE ? OR instructor LIKE ?
    """, ('%' + query + '%', '%' + query + '%'))
    results = c.fetchall()
    conn.close()
    return results