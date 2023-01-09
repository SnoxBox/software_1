"""ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä. 
Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, 
montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm."""

pituus = float(input("Kuha o kui pitkä?: "))
alipituus = 37

if (pituus <= alipituus):
    print(f"KUHA TAKAS JÄVEEN JA HETI PERKELE!!! SIITÄ PUUTTUU VIELÄ{(alipituus - pituus)} SENTTIÄ")
else:
    print("juu se o hyvä")


"""
Ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C)
ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. 
Tehtävässä on käytettävä if/elif/else-toistorakennetta.

    LUX on parvekkeellinen hytti yläkannella.
    A on ikkunallinen hytti autokannen yläpuolella.
    B on ikkunaton hytti autokannen yläpuolella.
    C on ikkunaton hytti autokannen alapuolella.

Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.
"""

hytti = str(input("mikäs o hyttis?: "))

match hytti:
    case 'LUX' | 'lux':
        print("LUX on parvekkeellinen hytti yläkannella.")
    case 'A' | 'a':
        print("A on ikkunallinen hytti autokannen yläpuolella.")
    case 'B' | 'b':
        print("B on ikkunaton hytti autokannen yläpuolella.")
    case 'C' | 'c':
        print("C on ikkunaton hytti autokannen alapuolella.")
    case _:
        print("Hyttiluokkaa ei löydy.")


"""ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). 
Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea."""

sukupuoli = input("Anna sukupuolesi (m/f): ")
hemo = float(input("Anna hemoglobiini arvosi (g/l): "))

# Tarkistetaan hemoglobiiniarvon normaalitilanne riippuen sukupuolesta
match sukupuoli:
    case 'm' | 'M':
        if 134 <= hemo <= 195:
            print("hemoglobiini on normaali")
        elif hemo < 134:
            print("hemoglobiini on alhainen")
        elif hemo > 195:
            print("hemoglobiini on liian korkea")
    case 'f' | 'F':
        if 117 <= hemo <= 175:
            print("hemoglobiini on normaali")
        elif hemo < 117:
            print("hemoglobiini on alhainen")
        elif hemo > 175:
            print("hemoglobiini on liian korkea")

"""ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi. 
Vuosi on karkausvuosi, jos se on jaollinen neljällä. 
Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla."""

vuosi = int(input("Syötä vuosi: "))

if ((vuosi % 4 == 0 and vuosi % 100 != 0) or vuosi % 400 == 0):
  print(str(vuosi) + " ei ole karkausvuosi")
else:
  print(str(vuosi) + " on karkausvuosi")