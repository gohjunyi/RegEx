import re

string = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', string)
# If-statement after search() tests if it succeeded
if match:
    print('found', match.group()) # 'found word:cat')
else:
    print('did not find')


# i+ = one or more i's, as many as possible.
match = re.search(r'pi+', 'piiig') # found, match.group() == "piii"

# Finds the first/leftmost solution, and within it drives the +
# as far as possible (aka 'leftmost and largest').
# In this example, note that it does not get to the second set of i's.
match = re.search(r'i+', 'piigiiii') # found, match.group() == "ii"

# \s* = zero or more whitespace chars
# Here look for 3 digits, possibly separated by whitespace.
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx') # found, match.group() == "1 2   3"
match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx') # found, match.group() == "12  3"
match = re.search(r'\d\s*\d\s*\d', 'xx123xx') # found, match.group() == "123"

# ^ = matches the start of string, so this fails:
match = re.search(r'^b\w+', 'foobar') # not found, match == None
# but without the ^ it succeeds:
match = re.search(r'b\w+', 'foobar') # found, match.group() == "bar"
