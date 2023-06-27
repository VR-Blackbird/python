import sys
import re
from collections import defaultdict

WORD_RE = re.compile(r"\w+")
index = defaultdict(list)


with open(sys.argv[1], encoding="UTF-8") as f:
    for line, text in enumerate(f, 1):
        for match in WORD_RE.finditer(text):
            word = match.group()
            column_no = match.start() + 1
            match_tup = (line, column_no)
            # index.setdefault(word, []).append(match_tup)
            index[word].append(match_tup)


print(dict(index))
