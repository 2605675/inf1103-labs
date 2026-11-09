from Product import Product


class Orderline:
    def __init__(self, product: Product, quantity: int) -> None:
        self.__product: Product = product
        self.__quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.__product.price * self.__quantity

    def display_order_line(self) -> str:
        return (
            f"{self.__product.display_information()}\n"
            f"Quantity: {self.__quantity}\n"
        )
