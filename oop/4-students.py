#!/usr/bin/python3

class Person:

    def __init__(self, name: str, id_number: int) -> None:
        self.name = name
        self.id_number = id_number


class Student(Person):

    def __init__(self, name: str, id_number: int, courses=[], grades=[]) -> None:
        super().__init__(name, id_number)
        self.courses = courses
        self.grades = grades

    def add_course_grade(self, course_name: str, course_grade: float) -> None:
        self.courses.append(course_name)
        self.grades.append(course_grade)

    def get_average_grade(self) -> float:
        if len(self.grades) > 0:
            return sum(self.grades) / len(self.grades)
        else:
            return 0.0

    def get_course_grade(self, course_name: str):
        if course_name in self.courses:
            index = self.courses.index(course_name)
            return self.grades[index]
        else:
            return None

    def get_courses(self) -> list:
        return self.courses


person1 = Person("John Smith", 12345)

assert person1.name == "John Smith"
assert person1.id_number == 12345

student1 = Student("Jane Doe", 67890)

assert student1.name == "Jane Doe"
assert student1.id_number == 67890
assert student1.courses == []
assert student1.grades == []

student1.add_course_grade("Math", 85.0)
student1.add_course_grade("English", 90.0)
student1.add_course_grade("Science", 95.0)

assert student1.get_average_grade() == 90.0
assert student1.get_course_grade("Math") == 85.0
assert student1.get_course_grade("History") is None
assert student1.get_courses() == ["Math", "English", "Science"]

student2 = Student("John Smith", 12345, ["History", "Art"], [92.0, 88.0])
assert student2.get_average_grade() == 90.0