# Week 6 Assignment: Safe Functions

This assignment practices catching errors with `try` and `except`, identifying specific errors, and keeping programs running instead of crashing.

## Files

- `safe_tools.py` - Contains three safe functions for division, number conversion, and dictionary field lookup.
- `unbreakable.py` - Demonstrates how to handle invalid user input without allowing the program to crash.
- `README.md` - Provides information about the assignment, files, and error-handling concepts.

## Why can the `if` check not catch `abc` on its own?

An `if` check can test conditions, but `int("abc")` causes Python to raise a `ValueError` during the conversion. The `try` and `except ValueError` structure catches this specific error and allows the program to continue instead of crashing.

## Expected Output from safe_tools.py

5.0
Cannot divide by zero
42
Not a number
82
Field not found