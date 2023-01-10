import random

"""
Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, 
joka saa parametrinaan nopeuden muutoksen (km/h). 
Jos nopeuden muutos on negatiivinen, auto hidastaa. 
Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.

Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. 
Jatka pääohjelmaa siten, 
että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. 
Tulosta tämän jälkeen auton nopeus. 
Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. 
Kuljettua matkaa ei tarvitse vielä päivittää.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

def main():
    auto = Auto("ABC-123", 142)
    print("Rekisteritunnus:", auto.rekisteritunnus)
    print("Huippunopeus:", auto.huippunopeus, "km/h")
    print("Tämänhetkinen nopeus:", auto.nopeus, "km/h")
    print("Kuljettu matka:", auto.matka, "km")
"""

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
    
    def accelerate(self, speed):
        self.nopeus += speed
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def travel(self, hours):
        self.matka += self.nopeus * hours

def main():
    cars = []

    for i in range(1, 11):
        rekisteri = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        cars.append(Auto(rekisteri, huippunopeus))

    while not any(car.matka >= 10000 for car in cars):
        for car in cars:
            muutos = random.randint(-10, 15)
            car.accelerate(muutos)
            car.travel(1)

    print("Rekisteritunnus | Huippunopeus | Nopeus      | Kuljettu matka")
    for car in cars:
        print(f"{car.rekisteritunnus}           | {car.huippunopeus} km/h     | {car.nopeus} km/h    | {car.matka} km") 

if __name__ == "__main__":
    main()