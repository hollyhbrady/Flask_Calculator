from flask import render_template
from app import app
from modules import calculator

@app.route('/add/2/3')
def add(int(2), int(3)): # getting invalid syntax, tried this and getting same error. I remember Hannah mentioned something about changing things from int to str or vise versa but 
    return f"The answer is{str(5)}"

@app.route('/subtract/6/2')
def subtract(6, 2):
    return f"The answer is{str(6, 2)}" #??

@app.route('/divide/10/5')
def divide(10, 5):
    return f"The answer is{str(2)}"

@app.route('/multiply/2/3')
def multiply(4, 3):
    return f"The answer is{str(12)}"


    