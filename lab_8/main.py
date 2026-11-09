from file_handle import file_handle
from Inventory import Inventory
from menu import menu
from supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Order import Order
from Orderline import Orderline

if __name__ == "__main__":
    handler = file_handle()
    my_inventory = Inventory()
    app = menu(handler, my_inventory)