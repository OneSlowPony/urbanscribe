from flask import Flask

from image_recognition import *
from geometric_algorithm import *


app = Flask(__name__)

@app.route("/")
def hello():
    return "We have data"

@app.route("/x")
def x():
    return "123"

@app.route("/y")
def y():
    return "456"


def angleInput():
    mainServo = int(input("Main Servo:  "))
    subServo = int(input("Main Servo: "))
    return mainServo, subServo


def coordInput():
    x = float(input("x  "))
    y = float(input("y: "))
    mainServo,subServo = coordsToAngles({
        "x":x,
        "y":y
        })
    return mainServo, subServo

@app.route("/data")
def data():

    mainServo, subServo = coordInput()
    print(str(mainServo) + "\n" + str(subServo) + "\n")
    return str(mainServo) + "\n" + str(subServo) + "\n" # chr(125) + chr(23)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
    print("After app")