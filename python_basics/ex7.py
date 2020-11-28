formatter = "{} {} {} {}" #ustanawiam zmienną dla ciągu znaków w cudzysłowiu

print(formatter.format(1, 2, 3, formatter)) #drukuje cyfry
print(formatter.format("jeden", "dwa", "trzy", "cztery")) #drukuje ciągi znaków
print(formatter.format(True, False, False, True)) #drukuje prawdę i fałsz
print(formatter.format(formatter, formatter, formatter, formatter)) #podstawia zmienną i drukują ją
print(formatter.format(
    "Karolina sprząta",
    "Jimmy lize",
    "Karol gra",
    "a korona trwa"
))