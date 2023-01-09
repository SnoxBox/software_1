"""
Kirjoita ohjelma, 
joka kysyy käyttäjältä kuukauden numeron, 
jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan 
(kevät, kesä, syksy, talvi). 
Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina 
monikkotietorakenteeseen. 
Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, 
että joulukuu on ensimmäinen talvikuukausi.
"""


def main():
    season = ["talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi"]
    month = int(input("Anna kuukauden numero (1-12): "))

    print(f"Kuukausi kuuluu vuodenaikaan: {season[month-1]}")

"""
Kirjoita ohjelma, 
joka kysyy käyttäjältä nimiä siihen saakka, 
kunnes käyttäjä syöttää tyhjän merkkijonon. 
Kunkin nimen syöttämisen jälkeen ohjelma tulostaa 
joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, 
syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee 
syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. 
Käytä joukkotietorakennetta nimien tallentamiseen.
"""

def main_2():
    names = []
    while True:
        name = input("Anna nimiä: ")
        if (name == ""):
            print("Suljetaan ohjelma...")
            break
        if (name in names):
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
            names.append(name)
            
    print("Syötetyt nimet:")
    for name in names:
        print(name)

"""
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. 
Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, 
hakea jo syötetyn lentoaseman tiedot vai lopettaa. 
Jos käyttäjä valitsee uuden lentoaseman syöttämisen, 
ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. 
Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa 
sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, 
ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon 
miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. 
(ICAO-koodi on lentoaseman yksilöivä tunniste. 
Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. 
Löydät koodeja helposti selaimen avulla.)
"""

import os

airports = {}

def main_3():

    menu = """
Valitse toiminto.
---------------------------------------------
[1] Syötä uusi lentoasema.
[2] Hae lentoaseman tietoja.
[3] Lopeta. 
---------------------------------------------"""


    while True:
        print(menu)
        choice = input("#> ")
        match choice:
            case '1':
                clear()
                kenttä = input("Anna lentokentän nimi: ")
                if (kenttä in airports):
                    print("Aiemmin syötetty kenttä")
                else:
                    koodi = input("Anna lentoaseman ICAO-koodin: ")
                    airports[kenttä] = koodi
                    input("Paina 'Enter' jatkaaksesi...")
                    clear()

                    print("Tiedot päivitetty:")
                    for kenttä, koodi in airports.items():
                        print(kenttä, "|", koodi)
                    input("Paina 'Enter' jatkaaksesi...")
                    clear()
            case '2':
                clear()
                koodi = search_airport_info(input("Anna kentän nimi: "))
                print(f"{koodi}")
                input("Paina 'Enter' jatkaaksesi...")
                clear()
            case '3':
                break
    
def search_airport_info(kenttä):
    neg_anwser = "Airport not found."
    pos_anwser = "Lentokentän ICAO-Koodi: "

    if kenttä in airports:
        return pos_anwser + airports[kenttä]
    elif kenttä not in airports:
        return neg_anwser

def clear():
    os.system('clear')

if __name__ == "__main__":
    main()
    main_2()
    main_3()