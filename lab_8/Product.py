from abc import ABC, abstractmethod
from supplier import Supplier


class Product(ABC):
    def __init__(self, product_id, name, price, stock, supplier):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)
        self.__supplier: Supplier = supplier

    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def stock(self):
        return self.__stock

    def update_stock(self, quantity):
        self.__stock = int(quantity)

    def display_information(self):
        return (
            f"ID: {self.__product_id} | Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | Stock: {self.__stock}"
        ), (self.display_supplier())

    def display_supplier(self):
        return f"{self.__supplier.display_information()}"

    @abstractmethod
    def get_fufilment_info(self):
        pass
