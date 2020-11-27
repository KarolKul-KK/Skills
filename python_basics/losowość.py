from random import randint

class losowy_kod(object):

    code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
    guess = input("[Keypad]> ")
    guesses = 0

    while guess != code and guesses < 10:
        print("BZZ")
        guesses += 1
        guess = input("[Keypad]> ")

    if guess == code:
        print("Trafiłeś, brawo")

    else:
        print("Nie zgadłeś")

    print(code)