"""
Assignment name: Derived Class Assignment
Program: Student.py
Author: Colby Boell
Last date modified: 04/03/2022

The purpose of this program is to use derived classes to get variables from another class (person) and allow
the other class (student) to use to store information and use the display function to display student info
"""

# import
from class_definitions.Person import Person


# student class
class Student(Person):
    def __init__(self, student_id, lname, fname,  major='Computer Science', gpa=0.0):
        super().__init__(lname, fname)
        self.student_id = student_id
        self.major = major
        self.gpa = gpa

    # display function
    def display(self):
        return f'{str(self._last_name)}, {str(self._first_name)}:({int(self.student_id)}) {str(self.major)} gpa: {float(self.gpa)}'


# Driver code
if __name__ == '__main__':
    my_student = Student(900111111, 'Song', 'River')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
    print(my_student.display())
    my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
    print(my_student.display())
    del my_student
