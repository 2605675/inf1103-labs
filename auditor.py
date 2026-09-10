inventory = 0
user_input = ""

while True:
    user_input = input("Enter a stock quantity: ")

    if user_input == "quit":
        break

    if user_input.isdigit():
        stock = int(user_input)
        inventory += stock
    elif user_input.startswith('-') and user_input[1:].replace('-', '', 1).isdigit():
        print("No negative number in user input")
        continue
    else:
        print("User input is not a integer")
        continue