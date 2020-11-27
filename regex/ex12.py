import re


pattern = re.compile(r'\w+(?=\sfox)')
result = pattern.search('the quick brown fox')
print(result.group())