
from app import app
from modules import calculator

@app.route('/')
def index():
    return "Hello, enjoy this calculator"

@app.route('/add/<x>/<y>')
def add(x, y):
    return f"The answer is {calculator.add(int(x), int(y))}"

@app.route('/subtract/<x>/<y>')
def subtract(x, y):
    return f"The answer is {calculator.subtract(int(x), int(y))}"

@app.route('/divide/<x>/<y>')
def divide(x, y):
    return f"The answer is {calculator.divide(int(x), int(y))}"

@app.route('/multiply/<x>/<y>')
def multiply(x, y):
    return f"The answer is {calculator.multiply(int(x), int(y))}"


    