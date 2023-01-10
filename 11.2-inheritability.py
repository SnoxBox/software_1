"""
Kirjoita aiemmin 
laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. 
Polttomoottoriauton ominaisuutena on bensatankin koko litroina.

Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa 
parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. 
Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi 
sekä asettaa oman kapasiteettinsa.

Kirjoita pääohjelma, 
jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) 
ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). 
Aseta kummallekin autolle haluamasi nopeus, käske autoja 
ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat
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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti
        self.nopeus = 0
        self.matka = 0

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankin_koko = bensatankin_koko
        self.nopeus = 0
        self.matka = 0

def main():
    sähköauto = Sähköauto("ABC-15", 180, 52.5)
    bensa_auto = Polttomoottoriauto("ACD-123", 165, 32.3)

    sähköauto.nopeus = 120
    bensa_auto.nopeus = 110

    sähköauto.travel(3)
    bensa_auto.travel(3)

    print(f"Sähköauto: {sähköauto.matka} km")
    print(f"Polttomoottoriauto: {bensa_auto.matka} km")

if __name__ == "__main__":
    main()