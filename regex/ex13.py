import re


"""
Match any word followed by a comma.
The example below is not the same as re.compile(r"\w+,")
For this will result in [ 'me,' , 'myself,' ]
"""

pattern = re.compile(r"\w+(?=,)")
res = pattern.findall("me, myself, adn I")
print(res)