#!/usr/bin/env python
"""mapper.py"""

import sys
import re

url_pattern = r'href="([^"]+)"' # Captures Wiki URL patterns

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # Find all matches for href="" in the current line
    urls = re.findall(url_pattern, line)

    for url in urls:
        print(f"{url}\t1")
    # increase counters
    # write the results to STDOUT (standard output);
    # what we output here will be the input for the
    # Reduce step, i.e. the input for reducer.py
    # tab-delimited; the trivial word count is 1
