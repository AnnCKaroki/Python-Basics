# Functions are reusable pieces of code that perform specific tasks.

# To declare a function we follow the syntax below:

# def nameoffunction(params):
#     indented code to be executed

# To run the code inside the function, we call as seen below:
# name(args)

# Example:(context of a school mangement system)
def calculate_average(grades): #grades is parameter
    return sum(grades) / len(grades)
    average = calculate_average(90, 85) #call the function with arguments
    print(f"Avg: {average}")

# Note that variables are labels that point to objects. All data(functions, list, strings) are objects in memory.
# Methods are functions that belong to an object. It performs speific action on or with the specified object's data.
# We call them using this syntax:
# object.method_name(arguments)
# Examples:
# A) String Methods (for student names, course titles, etc.)
student_name = "aLiCe wONDERLAND"
print(f"Original name: {student_name}")
print(f"Uppercase: {student_name.upper()}")   # Output: ALICE WONDERLAND
print(f"Lowercase: {student_name.lower()}")   # Output: alice wonderland
print(f"Capitalized: {student_name.capitalize()}") # Output: Alice wonderland
print(f"Replaced: {student_name.replace('Li', 'X')}") # Output: aXce wONDERLAND

# B) List Methods (for managing student rosters, class schedules)
class_roster = ["David", "Eve", "Frank"]
print(f"\nOriginal Roster: {class_roster}")
class_roster.append("Grace")        # Add an item to the end
print(f"After append: {class_roster}") # Output: ['David', 'Eve', 'Frank', 'Grace']
class_roster.remove("Eve")          # Remove a specific value
print(f"After remove: {class_roster}") # Output: ['David', 'Frank', 'Grace']
class_roster.sort()                 # Sort in-place
print(f"After sort: {class_roster}")   # Output: ['David', 'Frank', 'Grace']

# C) Dictionary Methods (for student profiles, course details)
student_profile = {"name": "Hannah", "grade": 10, "email": "h@school.com"}
print(f"\nStudent Profile: {student_profile}")
print(f"All keys: {student_profile.keys()}")     # Output: dict_keys(['name', 'grade', 'email'])
print(f"All values: {student_profile.values()}") # Output: dict_values(['Hannah', 10, 'h@school.com'])
print(f"Get email: {student_profile.get('email', 'N/A')}") # Get value safely
print(f"Get phone (default): {student_profile.get('phone', 'Not Set')}") # Key doesn't exist
# get method on a dictionary returns the value of the key you have specified but if it doesn't exist it retuns None instead of throwing an error


# Modules and Packages
# A module is a single file that ends in .py
# A package is a folder of related modules
# Importing brings code from modules to your python script
# import module: Access via module.item
# from module import item: Direct access to item
# import module as alias: Use alias.item
# Modules and sub-packages within a package are accessed using dot notation, for example, import package_name.module_name or from package_name.subpackage_name import module_name
