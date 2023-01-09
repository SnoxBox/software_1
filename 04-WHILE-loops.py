"""Kirjoita while-toistorakennetta käyttävä ohjelma,
joka tulostaa kolmella jaolliset luvut väliltä 1..1000."""

i = 1

while i in range(1000):
    while i <= 1000:
        if i % 3 == 0:
            print(i)
        i = i + 1


"""Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa 
negatiivisen tuumamäärän. 
Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm"""

tuuma = 0

while True:
    tuuma = float(input("Anna tuumamäärä: "))
    if (tuuma <= 0):
        break
    print(f"{tuuma} tuumaa on {(cm := tuuma * 2.54)} senttiä")


"""Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, 
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman."""

nums = []

while True:
    usr = input("Anna lukuja: ")
    if (usr == ""):
        print(f"pienin numero: {min(nums)}")
        print(f"isoin numero: {max(nums)}")
        break
    nums.append(int(usr))


"""Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. 
Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. 
Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. 
Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
"""

import random

num = str(random.randint(1, 10))

while True:
    usr = input("Arvaa luku 1-10 väliltä, kirjoita 'quit' poistuaksesi: ")
    if (usr in ['quit', 'Quit', 'QUIT']):
        print("Quitting...")
        break
    elif (usr > num):
        print("vastaus on pienempi")
    elif (usr < num):
        print("vastaus on isompi")
    else: 
        print(f"OIKEIN!, vastaus oli {num}")
        break


"""Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. 
Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. 
Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa. 
Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. 
(Oikea käyttäjätunnus on python ja salasana rules)."""

tries = 0
_usr = 'python'
_passwd = 'rules'

while tries in range(5):
    _usr = input("Username: ")
    _passwd = input("Password: ")

    match _usr:
        case 'python':
            match _passwd:
                case 'rules':
                    print("Tervetuloa")
                    break
                case _:
                    tries += 1
                    print("Pääsy evätty")
        case _:
            print("Pääsy evätty")
            tries += 1


"""Toteutetaan algoritmi piin (π) likiarvon laskemiseksi. 
Oletetaan, että A on yksikköympyrä eli ympyrä, jonka keskipiste on origossa ja jonka säde on yksi. 
Sen ympärille piirretään pienin mahdollinen neliö B siten, 
että ympyrä A jää kokonaan neliön sisäpuolelle. 
Neliön nurkkapisteet ovat tällöin (-1,-1), (1,-1), (1,1) ja (-1,1). 
Jos neliön sisälle arvotaan satunnaisesti suuri määrä pisteitä, 
osuu niistä myös ympyrän sisälle likimain niin suuri osuus kuin ympyrän pinta-ala on neliön pinta-alasta eli πr^2/4, 
joka (koska ympyrän säde on yksi) sievenee muotoon π/4. 
Tästä saadaan yksinkertainen menetelmä piin likiarvon laskemiseksi: 
Arvotaan neliön B sisälle suuri määrä satunnaisissa kohdissa olevia pisteitä, 
esimerkiksi miljoona. Olkoon N tämä pisteiden kokonaismäärä. 
Jokaisesta neliön B sisään arvotusta pisteestä testataan vuorollaan, 
jääkö se myös yksikköympyrän A sisälle. Olkoon n ympyrän sisälle jäävien pisteiden kokonaismäärä. 
Nyt pätee n/N≈π/4, josta saadaan π≈4n/N. Kirjoita ohjelma, 
joka kysyy arvottavien pisteiden määrän käyttäjältä ja toteuttaa piin likiarvon laskennan edellä kuvatulla menetelmällä. 
Lopuksi ohjelma tulostaa piin likiarvon käyttäjälle. 
(Huomaa, että jokaisesta arvotusta pisteestä (x,y) 
on helppoa testata onko se yksikköympyrän A sisällä: riittää testata, toteuttaako piste epäyhtälön x^2+y^2<1.)"""

import random

num_points = int(input("Anna arvottavien pisteiden määrä: "))

in_circle = 0
for i in range(num_points):
  x = random.uniform(-1, 1)
  y = random.uniform(-1, 1)
  
  if x**2 + y**2 < 1:
    in_circle += 1

pi = 4 * in_circle / num_points

print(f"Piin likiarvo: {pi:.4f}")