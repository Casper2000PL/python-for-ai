import requests

response = requests.get("https://api.github.com")

print(response.status_code)

# Variables
name = "Alice"
age = 30
is_student = False
height = 5.5
print(f"Name: {name}, Age: {age}, Student: {is_student}, Height: {height}")

# Comments
"""
Multi
line
comment
"""

# Strings
string = "My name is Alice."
my_long_string = """This is a long string that spans
multiple lines. It preserves
line breaks and spacing."""

name = "John"
last_name = "Doe"
full_name = name + " " + last_name
long_dash = "-" * 10
print(full_name)
print(long_dash)

len(full_name)

# Operators
a = 25
has_license = True
can_drive = a >= 18 and has_license
print(f"Can drive: {can_drive}")


first_name = "Jane"
last_name = "Doe"

# Using +
full_name = first_name + " " + last_name  # "Jane Doe"

# Using f-strings (modern Python way!)
greeting = f"Hello, {first_name}!"  # "Hello, Jane!"

# Multiple variables
age = 25
intro = f"I'm {first_name} and I'm {age} years old"

text = "Python Programming"

print(text.lower())      # "python programming"
print(text.upper())      # "PYTHON PROGRAMMING"
print(text.title())      # "Python Programming"

messy = "  hello world  "
print(messy.strip())     # "hello world" (removes whitespace)

price = "$19.99"
print(price.strip("$"))  # "19.99"

message = "I love Python programming with Python"

# Check if something exists
print("Python" in message)        # True
print(message.startswith("I"))   # True
print(message.endswith("Python")) # True

# Find position
print(message.find("Python"))     # 7 (first occurrence)
print(message.count("Python"))    # 2 (number of times)

# Replace
new_message = message.replace("Python", "JavaScript")
print(new_message)  # "I love JavaScript programming with JavaScript"
