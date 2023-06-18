def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def dedupe_advanced(items):
    seen = set()
    for item in items:
        val = tuple(item.items()) if isinstance(item, dict) else item
        if val not in seen:
            yield item
            seen.add(val)

print(list(dedupe_advanced([1,2,3,4,2,1,2,3])))
print(list(dedupe_advanced([{"x":10}, {"x":10}, 12, 11, 11])))
