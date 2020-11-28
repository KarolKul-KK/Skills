import re


def finder(string):
    """This function finds allthe word in a given string."""

    result_list = re.findall(r"\w+", string)
    print(result_list)

# call finder function, passing in the string argument
finder('finding dory habla bla bla')