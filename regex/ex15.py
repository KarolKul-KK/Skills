import re


pattern = re.compile(r"\w+\+") # match alphanumeric characters followed by a + character
result = pattern.search("file+")
print(result.group())