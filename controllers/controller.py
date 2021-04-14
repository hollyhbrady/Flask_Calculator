from flask import render_template
from app import app
from modules import calculator

@app.route('/add/2/3')
def add(2, 3):
    return f"The answer is{}"

@app.route('/subtract/6/2')
def subtract(6, 2):
    return f"The answer is{}"

@app.route('/divide/10/5')
def divide(10, 5):
    return f"The answer is{}"

@app.route('/multiply/2/3')
def multiply(4, 3):
    return f"The answer is{}"
    