from collections import defaultdict
from collections import OrderedDict
from collections.abc import Mapping, MutableSet

normal_dict = dict(name="Groot", age="12")
def_dict = defaultdict(list)
def_dict["aston"].append(190)

sets = set()

print(isinstance(normal_dict, dict))
print(isinstance(def_dict, dict))

print(isinstance(normal_dict, Mapping))
print(isinstance(def_dict, Mapping))
print(isinstance(sets, Mapping))
print(def_dict)
print(hash(sets))
