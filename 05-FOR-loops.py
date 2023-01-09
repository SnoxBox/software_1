"""Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän. 
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. 
Käytä for-toistorakennetta."""

import random

num = int(input("Anna arpakuutioiden määrä: "))
total = 0
i = 1

for i in range(num):
    print(f"Nopan {i}, luku on {(roll := random.randint(1, 6))}")
    total += roll
print(f"Arpakuutioiden summa on: {total}")


"""Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, 
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. d
Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen. 
Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True."""

nums = []
i = 0

while True:
    usr = input("Anna lukuja: ")
    if (usr == ""):
        nums.sort(reverse=True)
        print(nums[-i:])
        break
    nums.append(int(usr))
    i += 1


"""
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, 
onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut, 
jotka ovat jaollisia vain ykkösellä ja itsellään.

    -Esimerkiksi luku 13 on alkuluku, 
    koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.

    -Toisaalta esimerkiksi luku 21 ei ole alkuluku, 
    koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
"""

usr = int(input("Anna luku: "))

is_prime = True
for i in range(2, usr):
  if usr % i == 0:
    is_prime = False
    break

# Tulostetaan tulos
if is_prime:
  print("Luku on alkuluku.")
else:
  print("Luku ei ole alkuluku.")


"""Kirjoita ohjelma, 
joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan 
(käytä for-toistorakennetta nimien kysymiseen) 
ja tallentaa ne listarakenteeseen. 
Lopuksi ohjelma tulostaa kaupunkien nimet yksi 
kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin. 
käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta 
niiden läpikäymiseen."""

cities = []
i = 0


for i in range(5):
    usr = input("Anna kaupungin nimi: ")
    cities.append(usr)

for item in cities:
    print(item)