# Subsetting a list is similar to generating a small list from the main one.
# Syntax is: [start : end] Start is inclusive while end is exclusive. Make sure the start is before the end value
# We can achieve these using two methods:
# a) Negative indexing - gets the items at the end of the list
# For example:
religious_books = ["Bible", "Quran", "Book of Mormon", "Hebrew Bible"]
print(religious_books[-1]) #This will return the Hebrew Bible
# b) Zero indexing
# For example:
religious_books = ["Bible", "Quran", "Book of Mormon", "Hebrew Bible"]
print(religious_books[1:3]) #This will return Quran, Book of Mormon and Hebrew Bible

# To replace list elements, first subset the list element(s) to be replaced then assign them the new value.
# For example:
religious_books = ["Bible", "Quran", "Book of Mormon", "Hebrew Bible"]
# change Bible to Vedas
religious_books[0] = "Vedas" #assign new value
print(religious_books) #print the updated list

# To extend a list or add items to it we use the + operator
# For example:
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]

# To delete values from a list we use the del statement. The del statement works with positions or indexes only
# For example:
x = ["a", "b", "c", "d"]
del x[1] # deletes the item at index 1 which is b
# Removing using the pop method
# Note:
# pop() both removes an element and returns that element, allowing you to use it immediately.

# It works with both positive and negative indices.

# If no index is provided, it defaults to removing the last element (-1 index).

# It will raise an IndexError if you try to pop from an empty list or an invalid index.

#Removing using the remove method
#list.remove(value) #Removes the first occurrence of a specified value.
