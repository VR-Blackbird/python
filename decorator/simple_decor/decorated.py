from clock import clock
import time

@clock
def factorial(number):
    return 1 if number < 2 else number*factorial(number-1)

@clock
def snooze(seconds):
    time.sleep(seconds)


def main():
    print("Executing snooze\n")
    snooze(5)
    print("Executing facorial of a number\n")
    factorial(10)


if __name__ == '__main__':
    main()
