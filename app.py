"""Flask Web Application for a Simple Calculator"""

from flask import Flask, render_template, request

app = Flask(__name__)

def calculate(num1, num2, operation):
    """Performs arithmetic based on the selected operation"""
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == "add":
            return num1 + num2
        elif operation == "subtract":
            return num1 - num2
        elif operation == "multiply":
            return num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return "Cannot divide by zero"
            return num1 / num2
        return "Invalid operation"
    except ValueError:
        return "Invalid input"

@app.route("/", methods=["GET", "POST"])
def index():
    """Handles the form submission and result rendering"""
    result = None
    if request.method == "POST":
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        operation = request.form["operation"]
        result = calculate(num1, num2, operation)
    return render_template("index.html", result=result)

# if __name__ == "__main__":
#     app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
