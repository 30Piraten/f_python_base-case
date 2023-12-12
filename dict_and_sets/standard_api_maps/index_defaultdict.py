# Build an index mapping word -> list of occurrences

import re
import sys
import collections

REGEX_WORD = re.compile(r"\w+")

index = collections.defaultdict(list)
with open(sys.argv[0], encoding="utf-8") as fp:
    for line_number, line in enumerate(fp, 1):
        for match in REGEX_WORD.finditer(line):
            word = match.group()
            column_number = match.start()
            location = (line_number, column_number)
            index[word].append(location)

[print(word, index[word]) for word in sorted(index, key=str.upper)]
