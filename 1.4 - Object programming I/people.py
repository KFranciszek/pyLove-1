import json

class Czlowiek:
    bmi = 0
    roznicaWagiDoIdealu = 0
    def __init__(self, imie, waga, wzrost):
        self.waga = waga
        self.wzrost = wzrost * 0.01
        self.imie = imie

    def speak(self):
        print("Mowie prawde")

    def count_bmi(self):
        self.bmi = round(self.waga / ((self.wzrost) ** 2), 2) # zmienna bmi klasy czlowiek
        return self.bmi

    def diff_to_norm(self):
        if self.bmi < 18.5:
            oczekiwana_waga = 18.5 * (self.wzrost ** 2)
            self.roznicaWagiDoIdealu = round(oczekiwana_waga - self.waga, 2)
            return "Musisz przytyć {} kg.".format(self.roznicaWagiDoIdealu)
        elif self.bmi > 25.0:
            oczekiwana_waga = 25 * (self.wzrost ** 2)
            self.roznicaWagiDoIdealu = round(self.waga - oczekiwana_waga, 2)
            return "Musisz schudnąć {} kg.".format(self.roznicaWagiDoIdealu)
        else:
            return "Masz prawidłową wagę."


    def save_data(self):
         with open('{}.json'.format(self.imie), 'w') as file:
            json.dump(
                {'imie': self.imie,
                'waga': self.waga,
                 'wzrost': self.wzrost}, file)

    def timeToReachNormWeight(self, activity):
        time = self.roznicaWagiDoIdealu * 6000 / activity
        return time

    def to_burn(self):
            run, bike, hobby, chess = 500, 600, 250, 125

            print("Aby osiągnąć prawidłową wagę należy biegać {} godzin".format(self.timeToReachNormWeight(run)))
            print("Lub jeździć na rowerze przez {} godzin".format(self.timeToReachNormWeight(bike)))
            print("Można też uprawiać inne hobby przez {} godzin".format(self.timeToReachNormWeight(hobby)))
            print("W ostatecznosci można grać w szachy przez {} godzin".format(self.timeToReachNormWeight(chess)))

    def to_eat(self):
        choco = round(6000 * self.roznicaWagiDoIdealu / 4500, 1)
        potatos = round(6000 * self.roznicaWagiDoIdealu / 800, 1)

        print("Aby osiągnąć prawidłową wagę należy zjeść {} kg czekolady lub {} kg ziemniaków".format(choco, potatos))

    def what_to_do(self):
        return self.diff_to_norm()


class Polityk(Czlowiek):
    bribe = False
    def speak(self):
        if self.bribe:
            super().speak()
        else:
            print("Kłąmie, bo mogę")

    def recive_bribe(self):
        self.bribe = True



adam = Polityk("Aga", 80, 172,)
print(adam.imie)
adam.count_bmi()
print(adam.diff_to_norm())

if adam.bmi > 25:
    adam.to_burn()
elif adam.bmi < 18.5:
    adam.to_eat()
else:
    print("Waga prawidłowa")

print(adam.what_to_do())

# adam.save_data()
