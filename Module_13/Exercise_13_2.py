# Implement a backend service that gets the ICAO code of an airport and
# then returns the name and location of the airport in JSON format.
# The information is fetched from the airport database used on this course.
# For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK.
# The response must be in the format of:
# {
# "ICAO":"EFHK",
# "Name":"Helsinki-Vantaa Airport",
# "Location":"Helsinki"
# }

from flask import Flask, request
import mysql.connector

app = Flask(__name__)



@app.route("/airport/<icao>")
def c_airport_finder(icao):
    icao = icao
    sql = (f"SELECT name, ident, municipality FROM airport WHERE ident = '{icao}'")
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    json_result = {
        "ICAO" : result[0][1],
        "Name" : result[0][0],
        "Location" : result[0][2],
    }
    print(json_result)

    return json_result


connection = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        database='flight_game',
        user='dbuser',
        password='1234',
        autocommit=True,
    )

if __name__ == "__main__":
    app.run(use_reloader = True, host = "127.0.0.1", port = 5000)