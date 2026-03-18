# Salary Tracker

# This program defines an Employee class to track employee information and salary details. It includes validation for attribute types and values, as well as methods to update employee levels and salaries while ensuring that the new values meet certain criteria.
class Employee:
    _base_salaries = { # Class attribute to store base salaries for each level
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }

    def __init__(self, name, level): # To initialize an Employee object with name and level
        if not (isinstance(name, str) and isinstance(level, str)):
            raise TypeError("'name' and 'level' attribute must be of type 'str'.")
        if level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{level}' for 'level' attribute.")
        self._name = name
        self._level = level
        self._salary = Employee._base_salaries[level] # Set initial salary based on the level

    def __str__(self): # To return a string representation of the Employee object
        return f'{self.name}: {self.level}'

    def __repr__(self): # Returns a string representation of the Employee object for debugging 
        return f"Employee('{self.name}', '{self.level}')"

    @property # To turn the 'name' method into a property, the getter for the 'name' attribute
    def name(self):
        return self._name

    @name.setter # To define the setter for the 'name' attribute, allowing us to update the name of the employee
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")
        self._name = new_name
        print(f"'name' updated to '{self.name}'.")

    @property # To turn the 'level' method into a property, the getter for the 'level' attribute
    def level(self):
        return self._level

    @level.setter # To define the setter for the 'level' attribute, allowing us to update the level of the employee after validating the new level and ensuring that it is not a downgrade
    def level(self, new_level):
        if new_level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")
        if new_level == self.level:
            raise ValueError(f"'{self.level}' is already the selected level.")
        if Employee._base_salaries[new_level] < Employee._base_salaries[self.level]:
            raise ValueError(f"Cannot change to lower level.")
        print(f"'{self.name}' promoted to '{new_level}'.")
        self.salary = Employee._base_salaries[new_level]
        self._level = new_level

    @property # To turn the 'salary' method into a property, the getter for the 'salary' attribute
    def salary(self):
        return self._salary

    @salary.setter # To define the setter for the 'salary' attribute, allowing us to update the salary of the employee after validating that the new salary is a number and is higher than the minimum salary for the employee's level
    def salary(self, new_salary):
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")
        if new_salary <= Employee._base_salaries[self.level]:
            raise ValueError(f'Salary must be higher than minimum salary ${Employee._base_salaries[self.level]}.')
        self._salary = new_salary
        print(f'Salary updated to ${self.salary}.')


# Example usage
charlie_brown = Employee('Charlie Brown', 'trainee') # Employee object named 'Charlie Brown' with the level 'trainee'
print(charlie_brown)
print(f'Base salary: ${charlie_brown.salary}')
charlie_brown.level = 'junior'

# Output:
# Charlie Brown: trainee
# Base salary: $1000
# 'Charlie Brown' promoted to 'junior'.
# Salary updated to $2000.