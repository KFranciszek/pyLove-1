import json

class Czlowiek:
    bmi = 0
    def __init__(self, waga, wzrost, imie):
        self.waga = waga
        self.wzrost = wzrost
        self.imie = imie

    def speak(self):
        print("Mowie prawde")

    def count_bmi(self):
        self.bmi = round(self.waga / ((self.wzrost * 0.01) ** 2), 2) # zmienna bmi w konstruktorze

    def diff_to_norm(self):
    #    self.waga_OK = 80 # self.bmi * (self.wzrost ** 2)
#3     self.diff = self.waga_OK - self.waga
  #      return self.diff

        if self.bmi < 18.5:
            oczekiwana_waga = 18.5 * self.wzrost ** 2
            roznica = oczekiwana_waga - self.waga
            print("Musisz schudnąć {}", format.(roznica))  # tu jestblad
        elif self.bmi > 25.0:
            oczekiwana_waga = 25 * self.wzrost ** 2
            roznica = self.waga - oczekiwana_waga
            print("Musisz przytyć {}", format.(roznica))  # tu jest blad

        """
        BMI = float(self.count_bmi())
        if BMI < 19.99:
            print("Masz niedowagę")
        elif BMI > 20 and BMI < 24.99:
            print("Masz prawidłową wagę")
        elif BMI > 25 and BMI < 29.99:
            print("Masz nadwagę")
        else:
            print("Masz otyłość")
    """
    def save_data(self):

        with open('{}.json'.format(self.imie) 'w') as file:
            json.dump(
                {'waga': self.waga}, file)

    def to_burn(self):
        pass

    def to_eat(self):
        pass

    def what_to_do(self):
        pass

class Polityk(Czlowiek):
    bribe = False
    def speak(self):
        if self.bribe:
            super().speak()
        else:
            print("Kłąmie, bo mogę")

    def recive_bribe(self):
        self.bribe = True



adam = Polityk(75, 180, "Adam")
print(adam.count_bmi())
print(adam.bmi)
print(adam.diff_to_norm())

