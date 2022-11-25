class DictMixins:
    __slots__ = ()

    def __getitem__(self, key):
        print("Getting Key", str(key))
        return super().__getitem__(key)


    def __setitem__(self, key, value):
        print(f"Setting Key {key}, value {value}")
        return super().__setitem__(key, value)

class OurDict(DictMixins, dict):
    pass

o = OurDict()
o['x'] = 10
print(o['x'])
