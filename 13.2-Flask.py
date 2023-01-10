"""
Toteuta taustapalvelu, 
joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja 
kaupungin JSON-muodossa. Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. 
Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK. 
Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.
"""

import mysql.connector as database
from flask import Flask, jsonify
app = Flask(__name__)

airports = {}

@app.route('/kenttä/<icao>', methods=['GET'])
def main(icao):
    name, municipality = search_airport_info(icao)
    if icao:
        return jsonify({"ICAO": icao, "Name": name, "Municipality": municipality})
    else:
        return jsonify(message='Lentokenttää ei löytynyt'), 404

def search_airport_info(code):
    connection = database.connect(
        user="user",
        password="password",
        host="localhost",
        database="flight_game")
    cursor = connection.cursor()
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)