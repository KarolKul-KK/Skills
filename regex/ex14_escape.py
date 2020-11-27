import re


pattern= re.compile('\\\\')
result = pattern.match("\\author")
print(result.group()) #will print