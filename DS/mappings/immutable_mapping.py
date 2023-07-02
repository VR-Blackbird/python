from types import MappingProxyType

_d = {"1": 12, "2": 13}
dynamic_proxy = MappingProxyType(_d)

print(dynamic_proxy)
# dynamic_proxy["1"] = 15  Throw error as values cannot be changed

_d["14"] = 100
print(dynamic_proxy)
