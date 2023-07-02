from collections import Counter


alpha_count = Counter("abracadabra")
alpha_count.update("asda")

print(alpha_count.most_common(2))
print(list(alpha_count.keys())[0])
