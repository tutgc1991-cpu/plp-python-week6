# Week 6 Assignment: Unbreakable Program
# This program handles invalid input without crashing.


print("Welcome to the Unbreakable Number Program!")
print("Enter a whole number.")
print("Type 'q' to quit.")

while True:
    user_input = input("Enter a number: ")

    if user_input.lower() == "q":
        print("Program ended safely.")
        break

    try:
        number = int(user_input)
        print("You entered:", number)

    except ValueError:
        print("Invalid input. Please enter a whole number.")