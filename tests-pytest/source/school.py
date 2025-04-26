
class TooManyStudentsError(Exception):
    """Custom exception for too many students in a classroom."""
    pass


class Classroom:

    def __init__(self, teacher, students, course_title):
        self.teacher = teacher
        self.students = students
        self.course_title = course_title

    def add_student(self, student):
        if len(self.students) <= 10:
            self.students.append(student)
        else:
            raise TooManyStudentsError("Cannot add more than 10 students to a classroom.")

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return

    def change_teacher(self, teacher):
        self.teacher = teacher


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(Person):
    pass


class Student(Person):
    pass
