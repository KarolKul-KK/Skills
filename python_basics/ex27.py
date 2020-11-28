people = 1  #ustawia zmiennąo nazwie people i przypisuje jej wartość 1 
cars = 0 #to samo
trucks = 12 #to samo


if cars > people and people < trucks: #sprawdza czy cars jest większe od people jeśli tak to wyświetla tekst jeśli nie przechodzi do kolejnego warunku
    print("Powinniśmy jechać samochodami")
elif cars < people: #Jezeli pierwszy warunek nie zostanie spełniony program sprawdzi następny zdefiniowany jako elif
    print("Nie powinniśmy jechać samochodami.")
else: #jezeli zaden warunek nie zosatnie spelniony program wydrukuje to co po else
    print("Nie mozemy się zdecydować")

    print("Jest zbyt duzo cięzarówek.")
elif trucks < cars:
    print("Moze powinnniśmy wziąć ciezarówki")
else:
    print("Nadal nie mozemy się zdecydować")

if people > trucks:
    print("W Porządku, po prostu wezmy cięzarówki")
else:
    print("Dobra w takim razie zostajemy w domu.")