import mysql.connector as database
from geopy.distance import geodesic

"""
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. 
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen 
ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta. 
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
"""

connection = database.connect(
    user="user",
    password="password",
    host="localhost",
    database="flight_game")
cursor = connection.cursor()

airports = {}

def main():
    code = input("Anna kaksi ICAO-Koodi: ")
    code, municipality = search_airport_info(code)

    # Tulostetaan tiedot
    print(f"Lentoaseman nimi: {code}")
    print(f"Sijaintikunta (Municipality): {municipality}")


def search_airport_info(code):
    statement = "SELECT name, municipality from airport where airport.ident =%s"
    data = (code, )
    cursor.execute(statement, data)
    result = cursor.fetchone()

    # close connection
    cursor.close()
    connection.close()

    if result:
        return result
    else:
        return "", ""

def main_2():
    code = input("Anna maakoodi: ")
    search_airports(code)

def search_airports(code):
    statement = "SELECT type, COUNT(*) FROM airport WHERE iso_country = %s GROUP BY type"
    data = (code, )
    cursor.execute(statement, data)
    results = cursor.fetchall()

    for result in results:
        print(f'{result[0]} lentokenttiä: {result[1]}')

    # close connection
    cursor.close()
    connection.close()


"""
Ohjelma, 
joka kysyy käyttäjältä kahden lentokentän ICAO-koodit. 
Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä. 
Laskenta perustuu tietokannasta haettuihin koordinaatteihin. 
Laske etäisyys geopy-kirjaston avulla.
"""

def main_3():
    icao = input("Anna ensimmäisen lentoaseman ICAO-koodi: ")
    icao2 = input("Anna toisen lentoaseman ICAO-koodi: ")
    # Get the coordinates of the two airports
    coord1 = get_airports(icao)
    coord2 = get_airports(icao2)

    # Calculate the distance between the two airports
    distance = geodesic(coord1, coord2).km

    print("The distance between the two airports is:",distance,"km")

def get_airports(icao):
    connection = database.connect(
        user="user",
        password="password",
        host="localhost",
        database="flight_game")
    cursor = connection.cursor()
    statement = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    data = (icao,)
    cursor.execute(statement, data)
    coordinates = cursor.fetchone()

    # close connection
    cursor.close()
    connection.close()

    return coordinates

if __name__ == "__main__":
    main()
    main_2()
    main_3()