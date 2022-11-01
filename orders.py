
class Order:
    def __init__(self, amount, product) -> None:
        self.product = product
        self._amount = amount

    @property
    def amount(self):
        print("Ajsjs")
        return self._amount

    @amount.setter
    def amount(self, amount):
        raise OverflowError("Can't change")


o1 = Order(10, "Apples")

print(o1.amount)
o1.amount = 102
