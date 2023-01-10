import requests

"""
Kirjoita ohjelma, 
joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle. 
Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/. 
Käyttäjälle on näytettävä pelkkä vitsin teksti.
"""

def main():
    url = 'https://api.chucknorris.io/jokes/random'
    result = requests.get(url).json()
    print(result['value'])


"""
Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. 
Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. 

Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
"""

API_key = ''

def main_2():
    paikkakunta = str(input("Anna paikkakunna nimi: "))
    url = f"http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={API_key}&units=metric"
    weather = requests.get(url).json()

    kelvin_temp = weather['main']['temp'] + 273.15

    # tulostetaan säätila, lämpötila celsius ja lämpötila kelvin
    print(f"Säätila paikkakunnassa {paikkakunta}: {weather['weather'][0]['description']}")
    print(f"Lämpötila: {weather['main']['temp']} °C tai {kelvin_temp} K")

if __name__ == "__main__":
    main()
    main_2()