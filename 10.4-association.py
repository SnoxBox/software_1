"""
Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. 
Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi, 
pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, 
joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne 
ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin 
välein tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu 
kullekin autolle kulje-metodia.

tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi 
taulukoksi muotoiltuna.

kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut 
vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.

Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". 
Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. 
Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, 
jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. 
Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein 
sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.
"""

import random

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

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for car in self.autot:
            muutos = random.randint(-10, 15)
            car.accelerate(muutos)
            car.travel(1)

    def tulosta_tilanne(self):
        print("Rekisteritunnus | Huippunopeus | Nopeus      | Kuljettu matka")
        for car in self.autot:
            print(f"{car.rekisteritunnus}           | {car.huippunopeus} km/h     | {car.nopeus} km/h    | {car.matka} km") 

    def kilpailu_ohi(self):
        for car in self.autot:
            if car.matka >= self.pituus:
                self.tulosta_tilanne()
                print("---------- KILPAILU OHI!!!----------")
                return True
        return False

def main():
    cars = []

    for i in range(1, 11):
        rekisteri = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        cars.append(Auto(rekisteri, huippunopeus))

    kilpailu = Kilpailu("Suuri romuralli", 8000, cars)
    time = 0

    while not kilpailu.kilpailu_ohi():
        kilpailu.tunti_kuluu()
        time += 1
        if time % 10 == 0:
            kilpailu.tulosta_tilanne()
    kilpailu.tulosta_tilanne()

if __name__ == "__main__":
    main()