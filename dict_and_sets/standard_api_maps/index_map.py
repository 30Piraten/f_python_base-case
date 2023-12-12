# Test case: using dict.get
# Build an index mapping word -> list of occurrences

import re
import sys

REGEX_WORD = re.compile(r"\w+")

index = {}
with open(sys.argv[0], encoding="utf-8") as fp:
    for line_number, line in enumerate(fp, 1):
        for match in REGEX_WORD.finditer(line):
            word = match.group()
            column_number = match.start() + 1
            location = (line_number, column_number)
            #
            # dict.get --> index.get, is not the best
            # way to handle a missing key
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences
            #
for word in sorted(index, key=str.upper):
    print(word, index[word])
