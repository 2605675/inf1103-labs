from Orderline import Orderline
from Product import Product


class Order:
    def __init__(self, order_id: str) -> None:
        self.order_id: str = order_id
        self.order_lines: list[Orderline] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = Orderline(product, quantity)
        self.order_lines.append(order_line)

    def display_order_line(self) -> None:
        for order_line in self.order_lines:
            print(order_line.display_order_line())

    def calculate_total(self) -> float:
        return sum(order_line.calculate_subtotal() for order_line in self.order_lines)

    def remove_order_line(self, index: int) -> None:
        self.order_lines.pop(index)
