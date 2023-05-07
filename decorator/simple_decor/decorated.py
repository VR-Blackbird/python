from clock import clock
import time
import functools

@clock
def factorial(number):
    return 1 if number < 2 else number*factorial(number-1)

@clock
def snooze(seconds):
    time.sleep(seconds)

@functools.lru_cache
@clock
def fibonacci(number):
    if number < 2:
        return number
    else:
        return fibonacci(number-2) + fibonacci(number-1)

def main():
    print("Executing snooze\n")
    snooze(.12)
    print("Executing facorial of a number\n")
    factorial(10)
    print("Executing fibonacci series\n")
    fibonacci(30)


if __name__ == '__main__':
    main()
