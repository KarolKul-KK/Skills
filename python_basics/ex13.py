from sys import argv

script, user_name, nazwisko = argv
prompt = '! ' #Wykrzyknik to znak zachęty w naszym programie, mozemy go zastąpić kazdym innym znakiem.

print(f"Cześć, {user_name} {nazwisko}, jestem skryptem {script}.")
print("Chciałbym ci zadać kilka pytań.")
print(f"Lubisz mnie, {user_name}?")
likes = input(prompt)

print(f"Gdzie mieszkasz, {user_name}?")
lives = input(prompt)

print("Jaki masz komputer?")
computer = input(prompt)

print(f'''
Ok, gdy zapytałem, czy mnie lubisz, odpowiedziałeś {likes}.
Mieszkasz w {lives}. Nie jestem pewien gdzie to jest.
I masz komputer {computer}. Fajnie
''')