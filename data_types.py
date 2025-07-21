# Variables can store different data types.
# Different data types do different things.
# Python has built-in data types.
# Data types represents the value that tells what operations can be performed on a partiular data.

# We will use a scenario to understand the various data types that exist in python. Assume we are designing a basic school management system. We need to store information about the students, subjects, staff and school operations. We will use data types to achieve this goal.

# A) Numeric -  for quantities, scores or financial figures.
# int (integer)
student_age = 15
# float(numbers with decimals)
student_gpa = 4.0
# B) Sequence - for ordered collections of items
# string - For names, descriptions, or any text data. Immutable. Enclosed in single, double quootes.
# For example:
student_name = "Ann"
subject_title = 'Introduction to Python'
school_motto = """Backwards never,
Forward ever"""
# lists - for collections that can change. Enclosed in square brackets. Mutable(can add or remove)
# For example:
list_of_teachers = ["Omondi", "Diana", "Ratemo"]
# tuple - for fixed collection of items. Immutable. Enclosed in parathenses.
student_fixed_info =(1001, "Female", "07-22-2025")

# C) Mapping - stores data in key: value pairs. Keys are unique, values can be any type. Mutable.
# dict - unordered collection. Enclosed in curly brackets.
# For example:
student_profile = {
    "id": 1001,
    "name": "Alice Wonderland",
    "grade": 10,
    "email": "alice@school.edu",
    "is_active": True
}
# D) Set
# set - unique, unordered items. Mutable. Enclosed in curly braces. No duplicates allowed.
# For example:
enrolled_student_ids = {101, 105, 102, 101, 103, 105}

# E) Boolean - Represents truth values, either True or False. Capitalization is key!
# For example:
is_enrolled = True
is_course_full = False
# F) Binary
# bytes
# bytearray

# To check the type use the type function eg type(variable) inside the print function
# For example:
print(type(is_enrolled))
