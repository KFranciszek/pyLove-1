"""
# zadanie 1.1
def policz_slowa(str):
    templist = str.split(" ")
    ilosc = len(templist)
    print(ilosc)


policz_slowa("Ala ma kota")
policz_slowa("Pies psu niedzwiedziem, bo tak")

"""

"""
# zadanie 1.2
def policz_sam(text):
    sam = ("a", "e", "u", "o", "ą", "ó", "ę", "i")
  #  print(sam)
    text = text.lower()

    i = 0
    for letter in text:
       if letter in sam:
           i+=1
    return i


print(policz_sam("Ala ma kota"))
print(policz_sam("Pies psu niedzwiedziem"))
"""

"""
# zadanie 1.3 
def compare(text):
    o = 0
    x = 0
    for letter in text.lower():
        if letter == "o":
            o += 1
        elif letter == "x":
            x += 1
        else:
            return "Illegal letters in text"

    if o==x:
        return True
    else:
        return False

  #  return str(o) + "|" + str(x)

print(compare("xoxoxoxoxoxo"))
print(compare("xxxoooxxxxxxxo"))
print(compare("xpd"))
"""

"""
# zadanie 1.4
def cenzura_cyfr(text):
    newText=""
    for item in text:
        if item.isdigit():
            newText += "#"
        else:
            newText += item
    return newText

print(cenzura_cyfr("password12345"))
print(cenzura_cyfr("a1a ma k0ta"))
"""


"""
# Zadanie 1.5
from countries import countries

def countriesInSubregion(list, subregion):
    for item in list:
        if item['subregion']== subregion:
            print(item['name']['official'])

print(countriesInSubregion(countries, "Northern America"))
"""

"""
# Zadanie 1.6
from countries import countries

def countriesNotInRegion(list, region):
    for item in list:
        if item['region']!= region:
            print(item['name']['official'])

print(countriesNotInRegion(countries, "Africa"))
"""

"""
# Zadanie 1.7
from countries import countries

def countriesMultiCurrencies(list):
    for item in list:
        if len(item['currency']) > 1:
            print(item['name']['official'] + " ma więcej niż jedną walutę: " + ', '.join(item['currency']))


print(countriesMultiCurrencies(countries))
"""

"""
# Zadanie 1.8
from countries import countries

def countriesCapitalW(list):
    for item in list:
        if (item['capital']).startswith('W'):
            print('Stolicą ' + item['name']['official'] + ' jest ' + item['capital'])


print(countriesCapitalW(countries))
"""
"""
# Zadanie 1.9
from countries import countries

def biggestCountry(list):
    biggestArea = 0
    biggestCountry = ''
    for item in list:
        if (item['area']) > biggestArea:
            biggestArea = item['area']
            biggestCountry = item['name']['official']
    return biggestCountry + ' ma powierzchnie ' + str(biggestArea)+'km2' + " i jest największym krajem"


print(biggestCountry(countries))
"""

"""
# Zadanie 1.10
from countries import countries

def borderingCountries(list):
    borderCount = 0
    mostBordersCountry = ''
    for item in list:
        if len(item['borders']) > borderCount:
            borderCount = len(item['borders'])
            mostBordersCountry = item['name']['official']
    return 'Kraj o największej liczbie państw graniczących to ' + mostBordersCountry + ' ma ich ' + str(borderCount)


print(borderingCountries(countries))
"""
"""
# Zadanie 1.11
import math
def odwazniki(a, b) :
    x = math.gcd(a,b)
#   print(x)
    return (b//x, a//x)

print(odwazniki(2, 8))
print(odwazniki(4, 6))
"""
"""
#Zadanie 1.12
def droga(t, a, V = 0):
    S = V * t + (a * (t**2))/2
    return S

print(str(droga(5, 5)))
print(str(droga(10, 10, 100)))
"""

"""
# Zadanie 1.13
def cipher(txt, factor):
    if factor > 25 or factor < -25:
        return 'Przesuniecie poza zakresem'
    coded = ''
    for letter in txt:
        if letter.isalpha() and letter.islower():
            x = ord(letter) + factor
            if x < 97:
                x += 26
            elif x > 122:
                x -= 26
            coded += chr(x)
        elif letter.isalpha() and letter.isupper():
            x = ord(letter) + factor
            if x < 65:
                x += 26
            elif x > 90:
                x -= 26
            coded += chr(x)
        else:
            coded += letter
    return coded

print(cipher('abc',2))
print(cipher('ABC',-2))
"""