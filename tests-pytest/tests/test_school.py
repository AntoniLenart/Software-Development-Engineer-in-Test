# Made by AI

import pytest
from source.school import Classroom, Teacher, Student, TooManyStudentsError


@pytest.fixture
def sample_teacher():
    return Teacher(name="John Doe", age=35)


@pytest.fixture
def sample_students():
    return [Student(name=f"Student{i}", age=20+i) for i in range(5)]


@pytest.fixture
def full_classroom(sample_teacher, sample_students):
    return Classroom(teacher=sample_teacher, students=sample_students, course_title="Mathematics")


def test_initialization(full_classroom):
    assert full_classroom.teacher.name == "John Doe"
    assert full_classroom.course_title == "Mathematics"
    assert len(full_classroom.students) == 5


@pytest.mark.parametrize("student_name,expected_count", [ ("studenciak", 6), ("studenciak2", 6)])
def test_add_student_success(full_classroom, student_name, expected_count):
    new_student = Student(name="New Student", age=22)
    full_classroom.add_student(new_student)
    assert new_student in full_classroom.students
    assert len(full_classroom.students) == expected_count


def test_add_student_too_many(sample_teacher):
    students = [Student(name=f"Student{i}", age=20+i) for i in range(11)]
    classroom = Classroom(teacher=sample_teacher, students=students, course_title="Physics")

    with pytest.raises(TooManyStudentsError, match="Cannot add more than 10 students"):
        classroom.add_student(Student(name="Extra Student", age=30))


@pytest.mark.parametrize("student_name,expected_count", [
    ("Student1", 4),
    ("Student3", 4),
    ("NonExisting", 5),  # should not change
])
def test_remove_student(full_classroom, student_name, expected_count):
    full_classroom.remove_student(student_name)
    assert len(full_classroom.students) == expected_count
    assert all(student.name != student_name for student in full_classroom.students)


def test_change_teacher(full_classroom):
    new_teacher = Teacher(name="Jane Smith", age=40)
    full_classroom.change_teacher(new_teacher)
    assert full_classroom.teacher.name == "Jane Smith"
    assert full_classroom.teacher.age == 40
