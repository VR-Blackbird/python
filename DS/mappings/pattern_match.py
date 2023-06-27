def get_creators(record: dict) -> list:
    match record:
        case {"type": "book", "api": 2, "authors": [*names]}:
            return names
        case {"type": "book", "api": 1, "authors": name}:
            return [name]
        case {"type": "book"}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {"type": "movie", "director": name}:
            return [name]
        case _:
            raise ValueError(f"Invalid record: {record!r}")


print(get_creators({"type": "book", "api": 1, "authors": "johnson"}))

print(
    get_creators({"type": "book", "api": 2, "authors": "johnson kimber timber".split()})
)

new_dict = dict(type="book", api=1, authors="Brendon rodgers")
new_dict1 = dict(
    api=1, authors="Brendon rodgers", type="book"
)  # Order is different, but still matches

print(get_creators(new_dict))
print(get_creators(new_dict1))


def match_more(subject):
    match subject:
        case {"category": "ice cream", **details}:
            return f"Ice cream details: {details}"
        case _:
            raise ValueError(f"Invalid record: {subject!r}")


subject = dict(category="ice cream", flavor="vannila", cost=199)
print(match_more(subject))
