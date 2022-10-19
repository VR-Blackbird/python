def Boss():
    seq = 0

    def new():
        print("n = ", seq)

    def set_seq(value):
        nonlocal seq
        seq = value

    def get_seq():
        print(seq)

    new.set_seq = set_seq
    new.get_seq = get_seq

    return new


new = Boss()
new()
new.get_seq()
new.set_seq(12)
new.get_seq()
new()
