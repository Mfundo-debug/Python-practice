"""Both `re.match()` and `re.search()` are functions in Python's `re` module that are used to search for regular expression patterns in strings. However, they have some differences in how they work:

- `re.match()` searches for a pattern at the beginning of the string, while `re.search()` searches for a pattern anywhere in the string.
- `re.match()` only returns a match if the pattern is found at the beginning of the string, while `re.search()` returns the first match found in the string.
- `re.match()` is faster than `re.search()` because it only searches at the beginning of the string.

Here's an example to illustrate the difference:

"""

import re 

s = 'hello world'

#using re.match()
match = re.match('hello', s)
if match:
    print('match found:', match.group())
else:
    print('match not found')

#using re.search()
search = re.search('world', s)
if search:
    print('search found:', search.group())
else:
    print('search not found')