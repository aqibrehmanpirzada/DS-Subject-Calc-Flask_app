## Flask App Routing 
from flask import Flask,request,render_template


# create a simple flask app 
app = Flask(__name__)


# @app.route('/',methods=['GET'])
# def Welcome():
#     return "<h1>This is ARPZ Dead Wristler</h1>"

# @app.route('/index',methods=['GET'])
# def index():
#     return "<h2>Here is the Index Page</h2>"
# ## Variables Rules 
# @app.route('/add/<int:num1>/<int:num2>')
# def add(num1, num2):
#     result = num1 + num2
#     return f"The sum of {num1} and {num2} is {result}"

# @app.route('/subtract/<int:num1>/<int:num2>')
# def subtract(num1, num2):
#     result = num1 - num2
#     return f"{num1} minus {num2} is {result}"

# @app.route('/multiply/<int:num1>/<int:num2>')
# def multiply(num1, num2):
#     result = num1 * num2
#     return f"The product of {num1} and {num2} is {result}"

# @app.route('/divide/<int:num1>/<int:num2>')
# def divide(num1, num2):
#     if num2 == 0:
#         return "Error: Cannot divide by zero."
#     result = num1 / num2
#     return f"{num1} divided by {num2} is {result}"

## Displaying HTML pages
def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"

@app.route('/', methods=['GET', 'POST'])
def data_science_marks():
    if request.method == 'POST':
        subject1 = int(request.form['subject1'])
        subject2 = int(request.form['subject2'])
        subject3 = int(request.form['subject3'])
        subject4 = int(request.form['subject4'])

        average = (subject1 + subject2 + subject3 + subject4) / 4

        grades = {
            "Ethics of Data Science": calculate_grade(subject1),
            "Big Data": calculate_grade(subject2),
            "Machine Learning": calculate_grade(subject3),
            "Deep Learning": calculate_grade(subject4)
        }

        return render_template('results.html', average=average, grades=grades)

    return render_template('form.html')
if __name__ =='__main__':
    app.run(debug=True)
