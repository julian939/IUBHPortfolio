import manager.sqlmanager as sql
import objects.course_section as course_section

class Course:

    def __init__(self, id):
        self.id = id
        if self.exists():
            self.name = self.get_name()
            self.time = self.get_time()
            self.course_sections = self.get_course_sections()
        else:
            print("that course doesnt exist")
            return

    def exists(self) -> bool:
        result = sql.SQL().fetchone(f"SELECT EXISTS(SELECT 1 FROM course WHERE id={self.id})")[0]
        if result == 1:
            return True
        else:
            return False

    #GETTERS

    def get_name(self):
        result = sql.SQL().fetchone(f"SELECT name FROM course WHERE id={self.id}")
        return result[0]

    def get_course_sections(self):
        result = sql.SQL().fetchall(f"SELECT course_section_id FROM course_course_sections WHERE course_id={self.id}")
        result_list = []
        for id in result:
            curr_section = course_section.CourseSection(id[0])
            result_list.append(curr_section)
        return result_list

    def get_time(self):
        result = sql.SQL().fetchone(f"SELECT time FROM course WHERE id={self.id}")
        return result[0]

    #SETTERS

    def set_name(self, name):
        sql.SQL().execute(f"UPDATE course SET name={name} WHERE id={self.id}")

    def set_time(self, time):
        sql.SQL().execute(f"UPDATE course SET time={time} WHERE id={self.id}")
