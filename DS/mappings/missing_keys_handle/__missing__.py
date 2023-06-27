class UserDefinedDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, __key: object) -> bool:
        return __key in self.keys() or str(__key) in self.keys()


a = UserDefinedDict([("2", "two"), ("4", "four")])
print(a.get(3, []))
print(2 in a)
print(3 in a)
