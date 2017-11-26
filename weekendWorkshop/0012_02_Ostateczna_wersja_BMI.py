# ostateczna wersja BMI
print("Kalkulaor BMI")
sex =""
while sex !="M" and sex !="K":
    sex = input("Prosze podaj swoją płeć (M- meżczyzna, K- kobieta: ").upper()

if sex == "K":
    print("| %14s | %20s |" % ("BMI - Kobiety", "Klasyfikacja"))
    print("-" * 41 )
    print('| %14s | %20s |' % ('< 17,5', 'Niedowaga'))
    print("| %14s | %20s |" % ("17,5 – 22,49", "Prawidłowa waga"))
    print("| %14s | %20s |" % ("22,5 – 27,49", "Nadwaga"))
    print("| %14s | %20s |" % ("≥ 27,5", "Otyłość"))
else:
    print("| %14s | %20s |" % ("BMI - Mężczyźni", "Klasyfikacja"))
    print("-" * 41)
    print('| %14s | %20s |' % ('< 19.99', 'Niedowaga'))
    print("| %14s | %20s |" % ("20 – 24,99", "Prawidłowa waga"))
    print("| %14s | %20s |" % ("25,0 – 29,99", "Nadwaga"))
    print("| %14s | %20s |" % ("≥ 30,0", "Otyłość"))

weight = float(input("Teraz podaj swoją wage w kilogramach: "))
height = float(input("Na koniec podaj swój wzrost w centymetrach: ")) * 0.01

BMI = weight / (height * height)

if sex == "K":
    if BMI <17.5:
        print("Masz niedowagę")
    elif BMI > 17.5 and BMI < 22.49:
        print("Masz prawidłową wagę")
    elif BMI > 22.5 and BMI < 27.49:
        print("Masz nadwagę")
    else:
        print("Masz otyłość")
else:
    if BMI <19.99:
        print("Masz niedowagę")
    elif BMI > 20 and BMI < 24.99:
        print("Masz prawidłową wagę")
    elif BMI > 25 and BMI < 29.99:
        print("Masz nadwagę")
    else:
        print("Masz otyłość")
print("A Twój wskaźnik BMI wynosi " + "%.2f" % BMI)

print(input("Naciśnij dowolny klawisz aby zakończyć"))

