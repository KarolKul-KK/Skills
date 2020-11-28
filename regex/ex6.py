import re


pattern = re.compile(r"^<html>")
result = pattern.search("<html></html>")
print(result.group())