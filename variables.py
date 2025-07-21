# Variables store values that we will use  elsewhere in the code
# When they are used in code they represent or stand in for our value
# To declare or create a variable in Python we use = which is called an assignment operator
# For example:
name = "Ann"
# Python is dynamically typed thus we do not have to declare the data type of the value

# Naming Conventions:

# 1. A variable starts with a letter or underscore(_)
# 2. Variables can contain letters, numbers or underscores only
# 3. Variables are case sensitive hence name and Name are different
# 4. Mostly snake case is used when naming variables eg student_name


# Scope:
# Scope means the area or amount included. For example, when planning a conference the scope might include location, panel, food and registration process. It could exclude things live music and after party arrangments
# Variable scope defines where it is accessible and visible and usually follows the LEGB rule.
# L - local. In the example below a variable declared inside a function(my_function)is only accessible inside the function and can only be used inside it as they cease to exist outside the function.
def my_function():#function declaration in Python
    local_var = "I am local"
    print(local_var)
    #end of function
# E - enclosing. When an inner function refers to a variable that is not defined within it, python looks for the variable in the scope of the outer(enclosing) function
def outer_function():
    outer_var = "I am in the outer function"
    def inner_function():
        print(outer_var)
    inner_function()
outer_function()
# G - global. Variables declared at the top level of a script(file that ends in .py) can be accessed from anywhere in the program.
#The global keyword must be used when creating a global variable.
global_var = "I am global"

def access_global():
    print(global_var)

access_global()#to execute the block of code inside the function. Without it, nothing runs as we would only have defined.
# B - built-in. These are predifined functions and names. They are always available and accessible throughout the program without definition or import.
#For example:
print()
len
True
