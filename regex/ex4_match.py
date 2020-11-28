import re


line = "dance more"
result = re.match(r"[^\d+]", line)
print(result.group())