import os.path


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, "rb") as f:
        f.readinto(buf)
    return buf


with open("helper_files/sample.bin", "wb") as f:
    f.write(b"Hello world")

buf = read_into_buffer("helper_files/sample.bin")
buf[:5] = b"Hallo"
print(buf)
