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

@app.route('/Greet-Pages/Sanjay/')
def Sanjay():
    return render_template("Greet-Pages/Sanjay.html")

@app.route('/Greet-Pages/Matthew/')
def Matthew():
    return render_template("Greet-Pages/Matthew.html")

@app.route('/Greet-Pages/gavin/')
def gavin():
    return render_template("Greet-Pages/gavin.html")

@app.route('/Videos/')
def Videos():
    return render_template("Videos.html")

@app.route('/Greet-Pages/Greet/')
def Greet():
    return render_template("Greet-Pages/Greet.html")

@app.route('/greet_gavin', methods=['GET', 'POST'])
def greet_gavin():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Greet-Pages/gavin.html", name=name)
    # starting and empty input default
    return render_template("Greet-Pages/gavin.html", name="World")

@app.route('/greet_Sanjay', methods=['GET', 'POST'])
def greet_Sanjay():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Greet-Pages/Sanjay.html", name=name)
    # starting and empty input default
    return render_template("Greet-Pages/Sanjay.html", name="World")

@app.route('/greet_Matthew', methods=['GET', 'POST'])
def greet_Matthew():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Greet-Pages/Matthew.html", name=name)
    # starting and empty input default
    return render_template("Greet-Pages/Matthew.html", name="World")

if __name__ == "__main__":
    app.run(debug=True)
