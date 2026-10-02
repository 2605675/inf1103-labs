import json


def add_product():
    # get product id input
    product_id = input("Product ID: ")

    # get product name input
    input_product = input("Product Name: ")

    # get product price input
    Price = input("Price: ")

    input_quantity = input("Stock Quantity: ")

    if input_quantity == "quit":
        return "quit", 0, 0, 0

    if input_quantity.isdigit():
        input_quantity = int(input_quantity)
        return product_id, Price, input_product, input_quantity

    elif (
        input_quantity.startswith("-") and input_quantity.replace("-", "", 1).isdigit()
    ):
        print("No negative number in user input")
        return add_product()

    else:
        print("User input is not a integer")
        return add_product()

def update_stock(inventory):
    print("\nUpdate Stock")
    id = input("Enter Product ID: ")
    
    name = inventory[id]["Name"]
    stock = inventory[id]["Stock"]
    
    print("\nProduct Found:")
    print("Name: " + str(name))
    print("Current Stock: " + str(stock))
    
    new_stock = input("\nNew Stock Quantity: ")
    inventory[id]["Stock"] = new_stock
    
    print("\nStock updated successfully!")
    return inventory
    

def search_product(inventory):
    print("\nSearch Product")
    id = input("Enter Product ID: ")
    
    name = inventory[id]["Name"]
    price = inventory[id]["Price"]
    stock = inventory[id]["Stock"]
    
    print("\nProduct Found")
    print("------------------------------------------------")
    print("ID: " + str(id))
    print("Name: " + str(name))
    print("Price: " + str(price))
    print("Stock: " + str(stock))
    print("------------------------------------------------\n")
    
    

def load_inventory():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    try:
        with open("inventory.json", mode="r") as file:
            inventory = json.load(file)

            print("\ninventory.json found.")
            print("Inventory loaded successfully.\n")

    except (FileNotFoundError, ValueError):
        inventory = {}

    return inventory


def save_inventory(total, inventory):
    with open("inventory.txt", mode="w") as file:
        file.write(str(total) + "\n")

        for order in inventory:
            file.write(order + "\n")


def display_all(inventory):
    print("\nCurrent Inventory")
    print("------------------------------------------------")
    for id in inventory.keys():
        print(
            "ID: "
            + id
            + " | Name: "
            + inventory[id]["Name"]
            + " | Price: "
            + inventory[id]["Price"]
            + " | Stock: "
            + str(inventory[id]["Stock"])
        )
    print("------------------------------------------------\n")


def menu(inventory):
    print("----------- MENU -----------")
    print(
        "1. Display All Products\n2. Add Product\n3. Update Stock\n4. Search Product\n5. Save Inventory\n6. Exit"
    )
    print("----------------------------\n")

    option = input("Enter option: ")

    try:
        option = int(option)
    except:
        print("invalid input")
        return menu(inventory)

    if option == 1:
        display_all(inventory)
        return
    elif option == 2:
        print("\nAdd New Product")
        product_id, Price, input_product, input_quantity = add_product()
        inventory[product_id] = {
            "Name": input_product,
            "Price": "$" + str(Price),
            "Stock": input_quantity,
        }
        print("\nProduct added successfully\n")
    elif option == 3:
        update_stock(inventory)
    elif option == 4:
        search_product(inventory)
    elif option == 5:
        save_inventory(inventory)
    elif option == 6:
        print("Saving inventory before exit...")
        save_inventory(inventory)
        print("Inventory saved successfully.")
        
        print("Thank you for using Inventory Management System.\nProgram terminated.")
        return True
    
    return False

inventory = load_inventory()
quit = False

while not quit:
    quit = menu(inventory)
