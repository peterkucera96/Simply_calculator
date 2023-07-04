# Vytvorenie zakladov kalkualcky
print("Vitajte v kalkulacke")
operator = input("Vyberte operator(+ - * /): ")
cislo1 = float(input('Zadaj cislo 1: '))
cislo2 = float(input('Zadaj cislo 2: '))


# vetvenie pomocou if
if operator == '+':
    print('Sucet je: ', cislo1 + cislo2)
elif operator == '-':
    print('Rozdiel je: ', cislo1 - cislo2)
elif operator == '*':
    print('Sucin je: ', cislo1 * cislo2)
else:
    print('Deleno je: ', cislo1 / cislo2)


