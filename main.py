# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")



@app.route('/Videos/')
def Videos():
    return render_template("Videos.html")

@app.route('/Greet-Pages/Sanjay')
def Sanjay():
    return render_template("Greet-Pages/Sanjay.html")
# runs the application on the development server

@app.route('/Greet-Pages/Greet')
def Greet():
    return render_template("Greet-Pages/Greet.html")

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Sanjay.html", name=name)
    # starting and empty input default
    return render_template("Sanjay.html", name="World")

if __name__ == "__main__":
    app.run(debug=True)
