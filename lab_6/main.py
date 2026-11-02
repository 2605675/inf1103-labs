from file_handle import file_handle
from Inventory import Inventory
from menu import menu

if __name__ == "__main__":
    handler = file_handle()
    my_inventory = Inventory()
    app = menu(handler, my_inventory)