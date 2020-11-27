import re


string = "\n dreamer"
result = re.search(r"\w+", string, re.MULTILINE)
print(result.group())