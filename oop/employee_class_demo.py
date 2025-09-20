"""
Problem: Employee Class Example with Attribute Deletion
-------------------------------------------------------
We create an Employee class that demonstrates:
1. Object creation with attributes.
2. Displaying attributes using a method.
3. Deleting attributes and handling resulting errors.
"""

class Employee:
    def __init__(self, emp_id, emp_name):
        """
        Initialize an Employee object with:
        - emp_id: unique employee ID
        - emp_name: employee name
        """
        self.id = emp_id
        self.name = emp_name
    
    def display(self):
        """
        Display the employee's name and ID.
        Raises AttributeError if attributes are missing.
        """
        print(f"Name: {self.name}, ID: {self.id}")


# ------------------ DEMO ------------------
# Create an employee object
emp = Employee(1, "coder")
emp.display()  # Expected output: Name: coder, ID: 1

# Delete the 'id' attribute
del emp.id

# Try to display again (should raise AttributeError)
try:
    emp.display()
except AttributeError as a:
    print("Error:", a)

# Delete the object itself
del emp
