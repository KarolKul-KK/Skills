#Ta funkcja jest podobna do skryptów z argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#to args jest niepotrzebnie bo mozemy zrobić po prostu tak.
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#teraz funkcja która przyjmuje jede argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# na końcu funkcja nie przyjmująca zadnych argumentów
def print_none():
    print("Ja nie mam nic")


print_two ("Karol", "Kulinski")
print_two_again("Karol", "Kulinski")
print_one("Karol")
print_none()