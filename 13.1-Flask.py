"""
Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei. Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
"""

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/alkuluku/<int:num>', methods=['GET'])
def check_prime(num):
    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    return jsonify({"Number": num, "isPrime": is_prime(num)})

if __name__ == '__main__':
    app.run(debug=True, port=3000)

