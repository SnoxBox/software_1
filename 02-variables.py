import math
import random

# kysy ja printtaa nimi
print(nimi := input("Anna nimesi: "), f"Hauska tavata, {nimi}")

# kysy säde ja palauta ympyrän pinta-ala
print(säde := input("Anna säde: "), f"pinta-ala on: {math.pi * int(säde)** 2}")

# kysy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
a, b = map(float, input("Anna suorakulmion kanta ja korkeus: ").split())
print(f"Suorakolmion piiri on: {(2 * (a + b))}")
print(f"Suorakulmion pinta-ala on: {(a * b)}")

# ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
a, b, c = map(float, input("Anna kolme kokonaislukua: ").split())
print(f"Summa: {(summa := a + b + c)}")
print(f"Tulo: {(a * b * c)}")
print(f"Keskiarvo: {(summa / 3)}")

leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("\nAnna leiviskät: "))
luodit = float(input("\nAnna leiviskät: "))

luoti = luodit * 13.3
naula = luoti * 20
leiviskä = naula * 32

total_grams = (leiviskä + naula + luoti)
kilogrammat = int(total_grams / 1000)
grammat = int(total_grams % 1000)

print(f"Massa on {kilogrammat} kilogrammaa ja {grammat} grammaa, grammoissa {total_grams}")

#ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
three_dig = ""
for i in range(3):
    num = str(random.randint(0, 9))
    three_dig += num

four_dig = ""
for i in range(4):
    num = str(random.randint(1, 6))
    four_dig += num

print("Kolmenumeroinen koodi:", three_dig)
print("Nelinumeroinen koodi:", four_dig)