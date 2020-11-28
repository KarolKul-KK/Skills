import re

pattern = re.compile(r"\w+")
# Let's feed in some strings to match

string = "regex is awesome!"
# Thencall a matching method to match our pattern

result = pattern.match(string)
print(result.group()) # will print out 'r'