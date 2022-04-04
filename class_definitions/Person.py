"""
Assignment name: Derived Class Assignment
Program: Person.py
Author: Colby Boell
Last date modified: 04/03/2022

The purpose of this program is to use derived classes to get variables from another class (person) and allow
the other class (student) to use to store information and use the display function to display student info
"""


class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):
        self._last_name = lname
        self._first_name = fname
        self._address = addy


    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address
