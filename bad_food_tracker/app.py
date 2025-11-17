from flask import Flask, render_template, request, redirect
import json
from datetime import datetime
import os
from pathlib import Path

app = Flask(__name__)

# Save data in user's home directory instead of app directory
USER_DATA_DIR = Path.home() / "BadFoodTracker"
USER_DATA_DIR.mkdir(exist_ok=True)
DATA_FILE = USER_DATA_DIR / "data.json"

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
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

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
    # IMPORTANT: Set debug=False for production/distribution
    app.run(debug=False, host='127.0.0.1', port=5000)
