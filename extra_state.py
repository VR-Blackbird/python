# class Handler:
#     def __init__(self) -> None:
#         self.sequence = 0

#     def seq_handler(self, result):
#         self.sequence += 1
#         print(f"[{self.sequence}]   {result}")


# def Handler():
#     sequence = 0

#     def seq_handler(result):
#         nonlocal sequence
#         sequence += 1
#         print(f"[{sequence}]   {result}")

#     return seq_handler


def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print("[{}] Got: {}".format(sequence, result))


def add(x, y):
    return x + y


def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


seq = make_handler()
next(seq)
apply_async(add, (1, 13), callback=seq.send)
apply_async(add, (1, 23), callback=seq.send)
