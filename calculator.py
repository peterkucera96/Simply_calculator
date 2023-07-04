# Program kalkulacky
print("Vitajte v kalkulacke")
opakovanie = True
while opakovanie:
    operator = None
    while operator not in ['+', '-', '*', '/']:
        operator = input("Vyberte operator (+ - * /): ")
        if operator not in ['+', '-', '*', '/']:
            print('Chyba: Zadali ste nespravny operator!')

    
    while True:
        try:
            cislo1 = float(input("Zadajte číslo 1: "))
            break
        except ValueError:
            print("Chyba: Zadali ste nesprávne číslo!")

    while True:
        try:
            cislo2 = float(input("Zadajte číslo 2: "))
            break
        except ValueError:
            print("Chyba: Zadali ste nesprávne číslo!")


    if operator == '+':
        print('Vysledok je: ', cislo1 + cislo2)
    elif operator == '-':
        print('Vysledok je: ', cislo1 - cislo2)
    elif operator == '*':
        print('Vysledok je: ', cislo1 * cislo2)
    elif operator == '/':
        if cislo1 != 0:
            print('Cislom 0 sa neda delit.')
        else:
            print('Vysledok je: ', cislo1 / cislo2)

    pokracovat = input("Chcete pokračovať? (Y/N): ")
    if pokracovat.upper() != "Y":
        opakovanie = False

print('Dakujem ze ste pouzili kalkulacku.')