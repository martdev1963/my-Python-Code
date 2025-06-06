from flask import Flask, render_template

app = Flask(__name__)

import random

colors = ["Red", "Blue", "Green", "Pink", "Salmon", "Brown"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
months = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "November", "December"]
cars = ["Pinto", "Yugo", "Bug", "Lambo", "Ferrari"]

@app.route("/")
def home():
    return render_template('index.html', heading="What's lucky for you?")

@app.route("/cars")
def cheap_cars():
    car = random.choice(cars)
    return render_template('page.html', category='car', lucky_item=car,icon="car.png", heading="What's your lucky car?")

@app.route("/color")
def color_page():
    color = random.choice(colors)
    return render_template('page.html', category='color', lucky_item=color, icon="paint.png")

@app.route("/number")
def number_page():
    num = random.randint(1, 100)
    return render_template('page.html', category='number', lucky_item=num, icon="number.png")

@app.route("/week")
def week_page():
    weekday = random.choice(weekdays)
    return render_template('page.html', category='weekday', lucky_item=weekday, icon="calendar.png")

@app.route("/month")
def month_page():
    month = random.choice(months)
    return render_template('page.html', category='month', lucky_item=month, icon="calendar.png")
