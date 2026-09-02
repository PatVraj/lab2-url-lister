#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_url = None
current_count = 0
url = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    try:
        url, count = line.split('\t', 1) # parse the input we got from mapper.py
        count = int(count) # convert count (currently a string) to int        
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        # or the input from mapper didnt have a url and a count
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: url) before it is passed to the reducer
    if current_url == url:
        current_count += count
    else:
        if current_url and current_count > 5: #Need more than 5 occurences to output
            # write result to STDOUT
            print(f"{current_url}\t{current_count}")
        current_count = count
        current_url = url
            
# do not forget to output the last word if needed! Also needs the more than 5 occruences check
if current_url == url and current_count > 5:
    print(f"{current_url}\t{current_count}")

# cat input/file01 input/file02  | python URLMapper.py | sort | python URLReducer.py 