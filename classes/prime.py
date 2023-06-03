def is_prime(number):
    prime = True
    if number == 2:
        pass
    elif number <= 1:
        prime = False
    else:
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
    return prime


def get_prime_number(numbers: int) -> int:
    for number in range(numbers + 1):
        if is_prime(number):
            yield number


print(list(get_prime_number(100)))
