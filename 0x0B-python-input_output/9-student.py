#!/usr/bin/python3
<<<<<<< HEAD
"""``Student`` class module"""


class Student:
    """A class the represent a student"""

    def __init__(self, first_name, last_name, age):
        """Sets attributes of a new Student instance
            Args:
                first_name (str): The first name
                last_name (str): The last name
                age (int): The age
=======
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
>>>>>>> 64c4c9d375e4d43ef82a98094007d8606db1afdb
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
<<<<<<< HEAD
        """Returns a json represent of Student"""
        r = {}
        for key in self.__dict__:
            value = getattr(self, key)
            if type(value) in [list, dict, str, int, bool]:
                r[key] = value
        return r
=======
        """Get a dictionary representation of the Student."""
        return self.__dict__

>>>>>>> 64c4c9d375e4d43ef82a98094007d8606db1afdb
