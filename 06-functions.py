import random
import math

"""parametriton funktio, 
joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. 
Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. 
Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun."""

"""def main():
    while True:
        roll = dice_throw()
        print(f"Silmäluku: {roll}")
        if roll == 6:
            break

def dice_throw():
    return random.randint(1, 6)

if __name__ == "__main__":
    main()"""

"""Muokkaa edellistä funktiota siten, 
että funktio saa parametrinaan nopan tahkojen yhteismäärän. 
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. 
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes 
saadaan nopan maksimisilmäluku, 
joka kysytään käyttäjältä ohjelman suorituksen alussa."""

def main():
    side = int(input("How many sides does the die have?: "))
    while True:
        roll = dice_throw(side)
        print(f"Silmäluku: {roll}")
        if roll == side:
            break

def dice_throw(side):
    return random.randint(1, side)

"""
Kirjoita funktio, 
joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina 
ja palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, 
joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. 
Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, 
kunnes käyttäjä syöttää negatiivisen gallonamäärän.

Yksi gallona on 3,785 litraa.
"""

def main_2():
    while True:
        amount = float(input("Anna gallonamäärä: "))
        if (amount <= 0):
            print("Nolla tai alempi, suljetaan ohjelma")
            break
        print(calc(amount))

def calc(amount):
    return amount * 3.785


"""
Kirjoita funktio, 
joka saa parametrinaan listan kokonaislukuja. 
Ohjelma palauttaa listassa olevien lukujen summan. 
Kirjoita testausta varten pääohjelma, jossa luot listan, 
kutsut funktiota ja tulostat sen palauttaman summan.
"""

def main_3():
    nums = [1, 4, 6, 8]
    print(func2(nums))

def func2(nums):
    return sum(nums)

"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa toisen listan, 
joka on muuten samanlainen kuin parametrina saatu 
lista paitsi että siitä on karsittu pois kaikki parittomat luvut. 
Kirjoita testausta varten pääohjelma, jossa luot listan, 
kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.
"""

def main_4():

    og_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = rm_odds(og_nums)
    print(f"Alkuperäinen lista: {og_nums}")
    print(f"Karsittu lista: {evens}")

def rm_odds(og_nums):
    evens = []
  
    for number in og_nums:
        if number % 2 == 0:
            evens.append(number)
    
    return evens


"""
Kirjoita funktio, 
joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä 
sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan 
euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat 
ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle 
(eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa 
on hyödynnettävä kirjoitettua funktiota.
"""

def main_5():
    print("Anna ensimmäisen pizzan tiedot:")
    mitta1 = int(input("Halkaisija (cm): "))
    hinta1 = float(input("Hinta (€): "))

    print("Anna toisen pizzan tiedot:")
    mitta2 = int(input("Halkaisija (cm): "))
    hinta2 = float(input("Hinta (€): "))

    # Lasketaan pizzojen yksikköhinnat
    unit_price1 = unit_price(mitta1, hinta1)
    unit_price2 = unit_price(mitta2, hinta2)

    # Verrataan yksikköhintoja
    if unit_price1 < unit_price2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif unit_price1 > unit_price2:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Pizzat ovat saman hintaisia.")

def unit_price(mitta, hinta):
  pinta_ala = math.pi * (mitta / 2)**2
  
  yks_hinta = hinta / pinta_ala
  
  return yks_hinta


if __name__ == "__main__":
    #näitä on se kuus mut tää tiedosto on vähä päin persettä ko'ottu
    #1 löytyy kommenttina
    main()
    main_2()
    main_3()
    main_4()
    main_5()