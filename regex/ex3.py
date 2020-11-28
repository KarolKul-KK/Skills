import re

def regex(string):
    """This function returns at least one matching digit"""
    
    pattern = re.compile(r"\d{1,}") # fer brevity, this is the same as r"\d+
    result = pattern.match(string)

    if result:
        print(result.group())
    else:
        return None

#call our function, passing in our string
regex("007 James Bond")
