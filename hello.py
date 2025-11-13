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

# Empty list
my_list = []

# List with items
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]  # Different types OK!

fruits = ["apple", "banana", "orange"]

# Get items
print(fruits[0])    # "apple" (first item)
print(fruits[1])    # "banana"
print(fruits[-1])   # "orange" (last item)
print(fruits[-2])   # "banana" (second to last)

# Slicing
print(fruits[0:2])  # ["apple", "banana"]
print(fruits[1:])   # ["banana", "orange"]

fruits = ["apple", "banana", "orange"]

# Change an item
fruits[0] = "mango"
print(fruits)  # ["mango", "banana", "orange"]

# Add items
fruits.append("grape")      # Add to end
fruits.insert(1, "kiwi")    # Insert at position
print(fruits)

# Remove items
fruits.remove("banana")     # Remove by value
print(fruits)
last = fruits.pop()        # Remove and return last
print(fruits)
del fruits[0]              # Remove by index
print(fruits)

# Empty dictionary
my_dict = {}

# Dictionary with data
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Different ways to create
scores = dict(math=95, english=87, science=92)

person = {"name": "Alice", "age": 30, "city": "New York"}

# Get values by key
print(person["name"])       # "Alice"
print(person["age"])        # 30

# Safer with get()
print(person.get("job"))    # None (no error)
print(person.get("job", "Unknown"))  # "Unknown" (default)

person = {"name": "Alice", "age": 30}

# Add or update
person["email"] = "alice@email.com"  # Add new
print(person)
person["age"] = 31                   # Update existing
print(person)

# Remove items
del person["email"]              # Remove by key
print(person)
age = person.pop("age")          # Remove and return
print(person)
person.clear()                   # Remove all items
print(person)

# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")

# Single item tuple needs comma!
single = (42,)  # Note the comma
not_tuple = (42)  # This is just 42 in parentheses

# Without parentheses (implicit)
coordinates = 10, 20

point = (3, 5)
colors = ("red", "green", "blue")

# Get items
print(point[0])      # 3
print(colors[-1])    # "blue"

# Slicing works too
print(colors[0:2])   # ("red", "green")

# Unpack values
point = (3, 5)
x, y = point  # x = 3, y = 5

# Multiple assignment
a, b, c = 1, 2, 3  # Same as (1, 2, 3)
print(a, b, c)

# Swap variables elegantly
x, y = y, x  # Swaps values!

# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}

colors = {"red", "blue"}

# Add items
colors.add("green")
print(colors)  # {'red', 'blue', 'green'}

# Remove items
colors.remove("blue")    # Error if not found
colors.discard("yellow") # No error if not found

# Check membership
if "red" in colors:
    print("Red is available")

names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(set(names))
print(unique_names)  # ['Alice', 'Bob', 'Charlie']

allowed_users = {"alice", "bob", "charlie"}

if "alice" in allowed_users:  # Very fast!
    print("Access granted")

