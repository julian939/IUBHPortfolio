import manager.sqlmanager as sql
import objects.course as course

class CourseSection():

    def __init__(self, id):
        self.id = id
        if self.exists():
            self.name = self.get_name()
            self.page_number = self.get_page_number()
            self.expense = self.get_expense()
            self.time = self.get_time()
        else:
            print("that course section doesnt exist")
            return

    def exists(self):
        result = sql.SQL().fetchone(f"SELECT EXISTS(SELECT 1 FROM course_section WHERE id={self.id})")[0]
        if result == 1:
            return True
        else:
            return False

    #GETTERS

    def get_name(self):
        result = sql.SQL().fetchone(f"SELECT name FROM course_section WHERE id={self.id}")
        return result[0]

    def get_page_number(self):
        result = sql.SQL().fetchone(f"SELECT page_number FROM course_section WHERE id={self.id}")
        return result[0]

    def get_expense(self):
        result = sql.SQL().fetchone(f"SELECT expense FROM course_section WHERE id={self.id}")
        return result[0]

    def get_time(self):
        result = sql.SQL().fetchone(f"SELECT time FROM course_section WHERE id={self.id}")
        return result[0]

    #SETTERS

    def set_name(self, name):
        sql.SQL().execute(f"UPDATE course_section SET name={name} WHERE id={self.id}")

    def set_page_number(self, page_number):
        sql.SQL().execute(f"UPDATE course_section SET page_number={page_number} WHERE id={self.id}")

    def set_expense(self, expense):
        sql.SQL().execute(f"UPDATE course_section SET expense={expense} WHERE id={self.id}")

    def set_time(self, time):
        sql.SQL().execute(f"UPDATE course_section SET time={time} WHERE id={self.id}")
