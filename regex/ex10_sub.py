import re


pattern = re.compile(r"[0-9]+")
result = pattern.sub("__", "there is only 1 thing 2 do")
print(result)