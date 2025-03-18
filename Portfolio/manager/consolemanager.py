import objects.course as course
import objects.course_section as course_section
import manager.objectmanager as manager

class ConsoleManager:
    def __init__(self):
        ...

    #method to handle user inputs
    def handle_input(self):
        x = input()
        args = x.split(" ")

        match args[0].lower(): #listens for certain keywords in console
            case "help": 
                self.show_help_screen()
            case "createcourse": 
                if len(args) == 3:
                    try:
                        manager.ObjectManager().add_course(args[1], args[2])
                        print("Course created!")
                    except:
                        print("An error ocurred. Unknown ID")
                else:
                    print("Incorrect arguments. Please use createcourse <name> <time>")
            case "removecourse":
                if len(args) == 2:
                    try:
                        manager.ObjectManager().remove_course(args[1])
                        print("Course removed!")
                    except:
                        print("An error ocurred. Unknown ID")
                else:
                    print("Incorrect arguments. Please use removecourse <id>")
            case "createcoursesection":
                if len(args) == 5:
                    try:
                        manager.ObjectManager().add_course_section(args[1], args[2], args[3], args[4])
                        print("Coursesection created!")
                    except:
                        print("An error ocurred. Please try with different values")
                else:
                    print("Incorrect arguments. Please use createcoursesection <course_id> <name> <page_number> <expense>")
            case "removecoursesection":
                if len(args) == 2:
                    try:
                        manager.ObjectManager().remove_course_section(args[1])
                        print("Coursesection removed!")
                    except:
                        print("An error ocurred. Unknown ID")
                else:
                    print("Incorrect arguments. Please use removecoursesection <id>")
            case "takecoursesection":
                if len(args) == 2:
                    try:
                        manager.ObjectManager().set_active_course_section(args[1])
                        print("Coursesection taken successfull!")
                    except:
                        print("An error ocurred. Unknown ID")
                else:
                    print("Incorrect arguments. Please use takecoursesection <id>")
            case "coursesectionlist": 
                self.show_course_section_list()
            case "courselist": 
                self.show_course_list()
            case "activecoursesection":
                try:
                    self.show_active_course_section()
                except:
                    print("Theres no active coursesection")
            case "coursesectiondetails":
                if len(args) == 2:
                    try:
                        self.show_course_section_details(args[1])
                    except:
                        print("An error ocurred. Unknown ID")
                else:
                    print("Incorrect arguments. Please use coursesectiondetails <id>")
            case "coursedetails":
                if len(args) == 2:
                    try:
                        self.show_course_details(args[1])
                    except:
                        print("An error ocurred. Unknown ID")
                else:
                    print("Incorrect arguments. Please use coursedetails <id>")
            case _:
                print("Command doesnt exist")

        self.handle_input()

    #prints a list of courses
    def show_course_list(self):
        sections = manager.ObjectManager().get_all_courses()
        
        show = "\n-- Course List --\n\n"

        for x in sections:
            show += f"ID:{x.id} | Name: {x.name} \n"

        print(show)

    #prints a list of coursesections
    def show_course_section_list(self):
        sections = manager.ObjectManager().get_all_course_sections()
        
        show = "\n-- Course Sections List --\n\n"

        for x in sections:
            show += f"ID:{x.id} | Name: {x.name} \n"

        print(show)

    #prints the active coursesection
    def show_active_course_section(self):
        self.show_course_section_details(manager.ObjectManager().get_active_course_section_id())

    #prints details of coursesection with certain id
    def show_course_section_details(self, id):
        section = course_section.CourseSection(id)
        show = f"\n-- {section.name} | ID:{id} --\nPages: {section.page_number}\nExpense: {section.expense}\nTime: {self.get_time_from_seconds(section.time)}\n"
        print(show)

    #prints details of course with certain id
    def show_course_details(self, id):
        curr_course = course.Course(id)
        show = f"\n-- {curr_course.name} | ID:{id} --\nTime: {self.get_time_from_seconds(curr_course.time)}\nSections:\n"
        for x in curr_course.course_sections:
            show += f"  ID:{x.id} | Name: {x.name} | Time: {self.get_time_from_seconds(x.time)} \n"
        print(show)

    #prints starting screen
    def show_starting_screen(self):
        show = """
         ___________________
        |                   |
        |    --Started--    |
        | type help to view |
        |     commands      |
        |___________________|
        """
        print(show)
        self.handle_input()

    #prints help screen
    def show_help_screen(self):
        show = """
 _______________________________________
|               Commands                |
|---------------------------------------|
|  help                                 |
|  createCourse <name> <time>           |
|  removeCourse <id>                    |
|  createCourseSection <name> <time>    |
|  removeCourseSection <id>             |
|  takeCourseSection <id>               |
|  courseSectionList                    |
|  courseList                           |
|  activeCourseSection                  |
|  courseSectionDetails <id>            |
|  courseDetails <id>                   |
|_______________________________________|
"""
        print(show)

    #converts seconds to normal time values
    def get_time_from_seconds(self, seconds):
        if seconds < 86400:
            hours = round(seconds/3600)
            return str(hours) + "h"
        else:
            rest = round((seconds % 86400)/3600)
            days = round(seconds/86400)
            if rest != 0:
                return str(days) + "d " + str(rest) + "h"
            else:
                return str(days) + "d"