import random
class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        if self._items:
            return self._items.pop()
        else:
            raise LookupError("Nothing in list")
    def __call__(self):
        return self.pick()
bingo = BingoCage(range(5))
print(bingo.pick())
print(callable(bingo))
print(bingo())
