import re


pattern = re.compile(r"\w+") # Match only aplhanumeric characters
input_string = "Lorem ipsum with steroids"
result = pattern.sub("regex", input_string) # replace with the word regex
print(result)