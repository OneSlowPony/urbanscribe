from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "We have data"

@app.route("/data")
def data():
    return "123\n456\n" # chr(125) + chr(23)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
    print("After app")