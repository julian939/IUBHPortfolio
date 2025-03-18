import manager.sqlmanager as sql
import objects.course as course
import objects.course_section as course_section

class ObjectManager:

    def __init__(self):
        ...

    #creates a new course
    def add_course(self, name, time):
        curr_time = self.convert_to_seconds(time)
        sql.SQL().execute(f"INSERT INTO course (name, time) VALUES ('{name}', {curr_time})")

    #creates a new coursesection and adds it to the course 
    def add_course_section(self, course_id, name, page_number, expense):
        course_section_id = sql.SQL().execute_return(f"INSERT INTO course_section (name, page_number, expense, time, active) VALUES ('{name}', {page_number}, {expense}, 0, 0)")
        sql.SQL().execute(f"INSERT INTO course_course_sections (course_id, course_section_id) VALUES ({course_id}, {course_section_id})")
        self.calculate_course_section_times(course_id)

    #deletes a course
    def remove_course(self, id):
        curr_course = course.Course(id)
        for section in curr_course.course_sections:
            curr_id = section.id
            self.remove_course_section(curr_id)
        sql.SQL().execute(f"DELETE FROM course WHERE id={id}")

    #deletes a coursesection and removes it from the course 
    def remove_course_section(self, id):
        course_id = sql.SQL().fetchone(f"SELECT course_id FROM course_course_sections WHERE course_section_id={id}")[0]
        sql.SQL().execute(f"DELETE FROM course_section WHERE id={id}")
        sql.SQL().execute(f"DELETE FROM course_course_sections WHERE course_section_id={id}")
        self.calculate_course_section_times(course_id)
    
    #convert normal time values to seconds
    def convert_to_seconds(self, s):  
        seconds_per_unit = {"s": 1, "m": 60, "h": 3600, "d": 86400, "sec": 1, "min": 60}
        return int(s[:-1]) * seconds_per_unit[s[-1]]
    
    #calculates coursesection times dependand on their expense and page numbers
    def calculate_course_section_times(self, course_id):
        curr_course = course.Course(course_id)
        sections_list = curr_course.course_sections
        all_sections_points = 0
        for section in sections_list:
            all_sections_points += (section.page_number * section.expense)

        for section in sections_list:
            curr_section_points = (section.page_number * section.expense)
            new_time = (curr_section_points / all_sections_points) * curr_course.time
            section.set_time(new_time)

    #GETTERS

    def get_all_courses(self):
        result = sql.SQL().fetchall("SELECT id FROM course")
        result_list = []
        for id in result:
            curr_course = course.Course(id[0])
            result_list.append(curr_course)
        return result_list

    def get_all_course_sections(self):
        result = sql.SQL().fetchall("SELECT id FROM course_section")
        result_list = []
        for id in result:
            curr_section = course_section.CourseSection(id[0])
            result_list.append(curr_section)
        return result_list
    
    def get_active_course_section_id(self):
        result = sql.SQL().fetchone("SELECT id FROM course_section WHERE active=1")[0]
        return result
    
    #SETTERS

    def set_active_course_section(self, id):
        if course_section.CourseSection(id).exists():
            try:
                sql.SQL().execute(f"UPDATE course_section SET active=0 WHERE id={self.get_active_course_section_id()}")
            except:
                ...
            sql.SQL().execute(f"UPDATE course_section SET active=1 WHERE id={id}")