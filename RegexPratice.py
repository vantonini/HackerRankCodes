# The expression \D matches any character that is not a digit.
# The expression \d matches any digit [0-9].

Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.

import re

input = "06-11-2015"

print(str(bool(re.search(Regex_Pattern, input).lower())



Regex_Pattern = r'\w\w\w\W\w\w\w\w\w\w\w\w\w\w\W\w\w\w'	# Do not delete 'r'.
Regex_Pattern = r'(\w){3}\W(\w){10}\W(\w){3}'	# Do not delete 'r'.



Test_String = "www.hackerrank.com"
# Test_String = "123.456.abc.def"

# match = re.match(regex_pattern, Test_String) is not None
# count = re.findall(regex_pattern, Test_String)
print(str(bool(re.search(Regex_Pattern, Test_String))).lower())

# print(count)

# print(str(match).lower())


Regex_Pattern = r"^\d(\w){4}\.$"	# Do not delete 'r'.

import re

Test_String = "0qwer."


print(str(bool(re.search(Regex_Pattern, Test_String))).lower())



import re

Regex_Pattern = r'^[\D][^(aeiou)][^(bcDF)][(\S)][^(AEIOU)][^(\.\,)]$'	# Do not delete 'r'.


Test_String = "think??"
# Test_String = "123.456.abc.def"

# match = re.match(regex_pattern, Test_String) is not None
# count = re.findall(regex_pattern, Test_String)
print(str(bool(re.search(Regex_Pattern, Test_String))).lower())




import re

Regex_Pattern = r'^[a-zA-z02468]{40}[013579\s]{5}$'	# Do not delete 'r'.


Test_String = "x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo13957"
# Test_String = "123.456.abc.def"

# match = re.match(regex_pattern, Test_String) is not None
# count = re.findall(regex_pattern, Test_String)
print(str(bool(re.search(Regex_Pattern, Test_String))).lower())



import re

Regex_Pattern = r'^[\d]{1,2}[a-zA-Z]{3,}[.]{0,3}$'	# Do not delete 'r'.


Test_String = "3threeormorealphabets."
# Test_String = "123.456.abc.def"

# match = re.match(regex_pattern, Test_String) is not None
# count = re.findall(regex_pattern, Test_String)
print(str(bool(re.search(Regex_Pattern, Test_String))).lower())



import re

Regex_Pattern = r'^[\d]{2,}[a-z]*[A-Z]*$'	# Do not delete 'r'.


Test_String = "14."
# Test_String = "123.456.abc.def"

# match = re.match(regex_pattern, Test_String) is not None
# count = re.findall(regex_pattern, Test_String)
print(str(bool(re.search(Regex_Pattern, Test_String))).lower())



import re

# {0,1} can be '?'
Regex_Pattern = r'^tac(tac(tic){0,1})*$'	# Do not delete 'r'.


Test_String = "tactactic"
# Test_String = "tactactictactictictac"
# Test_String = "tactactictactictactactactactac"

# match = re.match(regex_pattern, Test_String) is not None
# count = re.findall(regex_pattern, Test_String)
print(str(bool(re.search(Regex_Pattern, Test_String))).lower())


import re

# {0,1} can be '?'
Regex_Pattern = r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)[a-z|A-Z]+$'	# Do not delete 'r'.


Test_String = "Mr.DOSHI"
Test_String = "Mr#DOSHI"
Test_String = "Mr.V.K. Doshi"
# Test_String = "tactactictactictictac"
# Test_String = "tactactictactictactactactactac"
# Test_String = "123.456.abc.def"

# match = re.match(regex_pattern, Test_String) is not None
# count = re.findall(regex_pattern, Test_String)
print(str(bool(re.search(Regex_Pattern, Test_String))).lower())










