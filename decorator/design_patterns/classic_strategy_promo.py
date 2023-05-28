# Promos available :
# Fidelity Promo(1000 or more fidelity points -> 5% per order),
# BulkItem Promo(20 or more Line Item -> 10% discount),
# LargeOrderPromo(Atleast 10 distinct items in cart -> 7% global discount)  #TODO

from abc import ABC, abstractmethod
from collections import namedtuple


cart = namedtuple("cart", ["product", "total_price", "number", "discount_price", "due"])


def apply_discounts(item, percentage):
    item.discount_price = item.total_price * percentage
    item.due = item.total_price - item.discount_price
    item.item = cart(
        item.product,
        item.total_price,
        item.number,
        item.discount_price,
        item.due,
    )


def FidelityPromo(person):
    if person.fidelity > 1000:
        for item in person.cart:
            apply_discounts(item, 0.05)


def BulkItemPromo(person):
    for item in person.cart:
        if item.number >= 20:
            apply_discounts(item, 0.1)


class Person:
    def __init__(self, name, fidelity) -> None:
        self.name = name
        self.fidelity = fidelity
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)

    def initiate_order(self, promo):
        promo(self)


class LineItem:
    def __init__(self, product, number, price) -> None:
        self.product = product
        self.number = number
        self.total_price = number * price
        self.discount_price = 0
        self.due = self.total_price
        self.item = cart(
            self.product, self.total_price, self.number, self.discount_price, self.due
        )


joe = Person("joe", 1000)
jim = Person("jim", 1111)


jim.add_to_cart(LineItem("apple", 20, 70))
jim.add_to_cart(LineItem("Banana", 17, 10))

jim.initiate_order(BulkItemPromo)
# print(joe.car[0].)
print(jim.cart[0].item)
print(jim.cart[1].item)
