from collections import UserDict


class UserDefinedDict0(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self.data[str(key)]

    def __contains__(self, key: object) -> bool:
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item


a = UserDefinedDict0([(2, "two"), ("4", "four")])
print(a)
print(2 in a)
print('4' in a)
