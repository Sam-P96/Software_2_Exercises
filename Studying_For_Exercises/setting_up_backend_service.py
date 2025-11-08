from flask import Flask, request

app = Flask(__name__)
@app.route('/sum')
def calculate_sum():
    args = request.args
    num1 = float(args.get("num1"))
    num2 = float(args.get("num2"))
    total_sum = num1 + num2

    response = {
        "num1" : num1,
        "num2" : num2,
        "total" : total_sum,
    }
    return response

@app.route("/echo/<text>")
def echo(text):
    response = {
        "echo" : text + " " + text
    }
    return response

if __name__ == "__main__":
    app.run(use_reloader = True, host = "127.0.0.1", port = 5000)