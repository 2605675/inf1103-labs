inventory = 0
user_input = ""

while True:
    user_input = input("Enter a stock quantity: ")

    if user_input == "quit":
        break

    stock = int(user_input)