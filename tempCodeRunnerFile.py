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
