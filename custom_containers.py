import collections.abc
import bisect


class CustomIterable(collections.abc.Iterable):
    def __iter__(self):
        pass


class CustomSequence(collections.abc.Sequence):
    def __init__(self, items=None):
        self._items = sorted(items) if items else []

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        bisect.insort(self._items, item)

    def delete(self, item):
        for index, value in enumerate(self._items):
            if value == item:
                del self._items[index]
                break
        else:
            print("Not available to delete")


class CustomMapping(collections.abc.Mapping):
    def __getitem__(self):
        pass

    def __len__(self):
        pass

    def __iter__(self):
        pass


# cust_iter = CustomIterable()
cust_seq = CustomSequence([4, 1, 2])
cust_mapping = CustomMapping()
print(list(cust_seq))
print(cust_seq[1])
cust_seq.add(0)
print(list(cust_seq))
cust_seq.delete(4)
print(list(cust_seq))
cust_seq.delete(41)


class CustomMutableSequence(collections.abc.MutableSequence):
    def __init__(self, items):
        self._items = list(items) if items else []

    def __delitem__(self, index):
        print(f"Deleting item at index {index}")
        del self._items[index]

    def __getitem__(self, index):
        print(f"Getting value for the index {index}")
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def __setitem__(self, index, item):
        print(f"Setting the value {item} in the index position {index}")
        self._items[index] = item

    def insert(self, index, value):
        print(f"Inserting the value {value} at the specified position {index}")
        self._items.insert(index, value)


cm = CustomMutableSequence([1, 4, 2])
cm.append(10)
print(list(cm))
cm.remove(4)
print(list(cm))
cm.insert(3, 12)
print(list(cm))
