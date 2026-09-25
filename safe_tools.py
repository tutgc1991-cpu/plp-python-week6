# Week 6 Assignment: Safe Functions
# This program demonstrates how to handle errors using try and except.


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


def safe_number(text):
    try:
        return int(text)
    except ValueError:
        return "Not a number"


def get_field(learner, key):
    try:
        return learner[key]
    except KeyError:
        return "Field not found"


# Test safe_divide()
print(safe_divide(10, 2))
print(safe_divide(10, 0))

# Test safe_number()
print(safe_number("42"))
print(safe_number("abc"))

# Test get_field()
learner = {"name": "Amina", "score": 82}
print(get_field(learner, "score"))
print(get_field(learner, "email"))