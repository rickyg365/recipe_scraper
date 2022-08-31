from dataclasses import dataclass


def input_shopping_item():
    data = {
        "name": input("Item Name: "),
        "quantity": int(input("Quantity: ")),
        "price": float(input("Price: ")),
        "store": input("Store Name: ")
    }
    return data


@dataclass
class ShoppingItem:
    name: str
    quantity: int
    price: float
    store: str
    total_price: float=0.0

    def __post_init__(self):
        self.total_price = self.quantity*self.price

    def __str__(self) -> str:
        txt = f"""${self.total_price:.2f} {self.name} ({self.quantity} @ ${self.price:.2f})"""
        return txt

    