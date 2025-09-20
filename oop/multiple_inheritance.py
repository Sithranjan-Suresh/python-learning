"""
Problem: Multiple Inheritance Example
-------------------------------------
Demonstrates multiple inheritance in Python:
1. Teacher and Youtuber are base classes.
2. Student inherits from both and can access methods from both parents.
"""

# Base class 1
class Teacher:
    def skills(self):
        """
        Skills specific to a Teacher
        """
        print("Teaching")

# Base class 2
class Youtuber:
    def skills(self):
        """
        Skills specific to a Youtuber
        """
        print("Making videos")

# Derived class inheriting from Teacher and Youtuber
class Student(Teacher, Youtuber):
    def skills(self):
        """
        Combine skills from both parent classes and add own skills
        """
        Teacher.skills(self)    # Call Teacher's skills
        Youtuber.skills(self)   # Call Youtuber's skills
        print("Studying")       # Student's own skill

# ------------------ DEMO ------------------
s = Student()
s.skills()
