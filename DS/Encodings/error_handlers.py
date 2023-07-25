import array
import pdb


e_str = "São Paulo"

print(e_str.encode("utf8"))
# try:
#     print(e_str.encode("cp437"))
# except UnicodeEncodeError as ue:
#     pdb.set_trace()

print(e_str.encode("cp437", errors="ignore"))
encoded = e_str.encode("cp437", errors="replace")

