from db import add_course, delete_course, get_all_courses

def test_add_and_delete():
    add_course("Python", "Dr. Smith", "Spring")
    courses = get_all_courses()
    assert any(c[0] == "Python" for c in courses)

    delete_course("Python")
    courses = get_all_courses()
    assert all(c[0] != "Python" for c in courses)

test_add_and_delete()
print("All tests passed.")