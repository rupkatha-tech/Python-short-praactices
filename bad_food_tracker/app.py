from flask import Flask, render_template, request, redirect
import json
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "data.json"

FOODS = [ 
    "Soda / Soft Drinks",
    "Fast Foods",
    "Eating Out",
    "Alcohol",
    "Palm Oil",
    "Deep Fried Chicken",
    "Fried Potatoes",
    "Popcorn",
    "Sugar",
    "Ice-Cream",
    "Oily / Greasy Foods",
    "Sweets",
    "White Bread",
    "White Rice"
]

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/", methods=["GET", "POST"])
def index():
    data = load_data()
    today = datetime.today().strftime("%Y-%m-%d")

    if request.method == "POST":
        values = request.form.getlist("foods")
        data[today] = values
        save_data(data)
        return redirect("/summary")

    return render_template("index.html", foods=FOODS)

@app.route("/summary")
def summary():
    data = load_data()
    return render_template("summary.html", data=data, foods=FOODS)

if __name__ == "__main__":
    app.run(debug=True)
