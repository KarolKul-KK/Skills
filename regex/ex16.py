import re


number = input("Enter your number\n")

def monetizer(number):
    """This function adds a thousands separator using comma characters."""
    number = str(number)
    try:
        if type(int(number)) == int:
            # format into groups of three from the right to the left
            pattern = re.compile(r'\d{1,3}(?=(\d{3})+(?!\d))')
            # substitute with a comma then return 
            return pattern.sub(r'\g<0>,', number)

    except:
        return "Not a number"

print(monetizer(number))