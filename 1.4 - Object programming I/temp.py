class Czlowiek:
    bmi = 0
    def __init__(self, imie, waga, wzrost):
        self.waga = waga
        self.wzrost = wzrost * 0.01
        self.imie = imie

    def speak(self):
        print("Mowie prawde")

class Polityk(Czlowiek):
    bribe = False
    def speak(self):
        if self.bribe:
            super().speak()
        else:
            print("Kłąmie, bo mogę")

    def recive_bribe(self):
        self.bribe = True

jarus = Polityk("Jaro", 87, 155)
miko = Czlowiek("Mikołaj", 65, 180)
print("Jaro: ")
jarus.speak()
print("Miko: ")
miko.speak()
print('Miko daje łapówkę')
jarus.recive_bribe()
print("Jaro: ")
jarus.speak()