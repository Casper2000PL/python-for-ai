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

# if-else Statements
score = 85

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")

age = 25
has_license = True
weekend = False
holiday = True
raining = False

# Both must be True
if age >= 18 and has_license:
    print("You can drive!")

# At least one must be True
if weekend or holiday:
    print("No work today!")

# Reverse the condition
if not raining:
    print("Let's go outside!")

# Loops
# Print numbers 0 through 4
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# Count from 1 to 5
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5

# Count by 2s
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8

name = "Python"
for letter in name:
    print(letter)

# Output:
# P
# y
# t
# h
# o
# n

colors = ["red", "blue", "green"]
for color in colors:
    print(f"I like {color}")

# Output:
# I like red
# I like blue
# I like green

count = 0
while count < 5:
    print(f"Count is {count}")
    count = count + 1  # Increase count by 1

# Output:
# Count is 0
# Count is 1
# Count is 2
# Count is 3
# Count is 4
