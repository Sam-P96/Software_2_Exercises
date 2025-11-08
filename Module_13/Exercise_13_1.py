# COPY-PASTE THIS TO MAKE YOUR LIFE EASIER: http://127.0.0.1:5000/prime_number?number_x=31
# COPY-PASTE THIS TO MAKE YOUR LIFE EASIER: http://127.0.0.1:5000/prime_number/31
# I made 2, cus oops. 🥲

from flask import Flask, request
import sympy

app = Flask(__name__)

@app.route("/prime_number")
def isit_prime():
    try:
        args = request.args
        number_x = int(args.get("number_x"))
        answer_x = sympy.isprime(number_x)
        json_return = {
            "Number" : number_x,
            "isPrime" : f"{answer_x}",
        }
        return json_return

    except ValueError:
        json_return_2 = {
            "Number" : "Error, not an integer",
            "isPrime" : "Error, not an integer"
        }
        return json_return_2

@app.route("/prime_number/<number>")
def primer(number):
    number = int(number)
    response = {
        "Number" : number,
        "isPrime" : sympy.isprime(number)
    }
    return response
if __name__ == "__main__":
    app.run(use_reloader = True, host = "127.0.0.1", port = 5000)