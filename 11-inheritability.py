"""
Toteuta seuraava luokkahierarkia Python-kielellä: 
Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi. 
Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. 

Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot, 
joka tudostaa kyseisen julkaisun kaikki tiedot. 

Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) 
ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). 
Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.
"""

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print("Nimi:", self.nimi)

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumäärä):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjailija: {self.kirjailija}")
        print(f"Sivumäärä: {self.sivumäärä}")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Pääkirjoittaja: {self.päätoimittaja}")

def main():
    kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
    lehti = Lehti("Aku Ankka", "Aki Hyyppä")

    print("Tiedot kirjasta:")
    kirja.tulosta_tiedot()

    print("Tiedot lehdestä:")
    lehti.tulosta_tiedot()

if __name__ == "__main__":
    main()