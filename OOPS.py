#Question_1

class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        Course.__init__(self, course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        Course.__init__(self, course_code, course_name, credit_hours)
        self.elective_type = elective_type

core_course_1 = CoreCourse("CS101", "Introduction to Computer Science", 4, True)
print(f"Core Course: {core_course_1.course_code} - {core_course_1.course_name}\nCredit Hours: {core_course_1.credit_hours}")
print(f"Required for major: {'Yes' if core_course_1.required_for_major else 'No'}")

elective_course_1 = ElectiveCourse("PB101", "Public Speaking", 3, "General")
print(f"Elective Course: {elective_course_1.course_code} - {elective_course_1.course_name}\nCredit Hours: {elective_course_1.credit_hours}")
print(f"Elective Type: {elective_course_1.elective_type}")


#Question_2

import Employee as e

emp1 = e.Employee("Sahal", 60000)
print("Employee Name:",emp1.get_name())
print("Employee Salary:",emp1.get_salary())

