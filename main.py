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

@app.route('/Sanjay/')
def Sanjay():
    return render_template("Sanjay.html")


@app.route('/samuel/')
def Samuel():
    return render_template("samuel.html")


@app.route('/Matthew/')
def Matthew():
    return render_template("Matthew.html")

@app.route('/gavin/')
def gavin():
    return render_template("gavin.html")

@app.route('/Videos/')
def Videos():
    return render_template("Videos.html")

@app.route('/MiniLabs/')
def MiniLabs():
    return render_template("MiniLabs.html")


@app.route('/greet_gavin', methods=['GET', 'POST'])
def greet_gavin():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Greet-Pages/templates/gavin.html", name=name)
    # starting and empty input default
    return render_template("gavin.html", name="World")

@app.route('/greet_Sanjay', methods=['GET', 'POST'])
def greet_Sanjay():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Sanjay.html", name=name)
    # starting and empty input default
    return render_template("Sanjay.html", name="World")

@app.route("/binary/", methods = ['GET', 'POST'])
def binary():
    BITS = 4
    imgBulbOn = "/static/assets/bulb_on.gif"
    # second time you call it, its a post action
    if request.method == 'POST':
        BITS = int(request.form['BITS'])
        imgBulbOn = request.form['lightOn']
    return render_template("binary.html", imgBulbOn=imgBulbOn, BITS=BITS)

@app.route('/greet_Matthew', methods=['GET', 'POST'])
def greet_Matthew():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Matthew.html", name=name)
    # starting and empty input default
    return render_template("Matthew.html", name="World")

@app.route('/greet_samuel', methods=['GET', 'POST'])
def greet_samuel():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("samuel.html", name=name)
    # starting and empty input default
    return render_template("samuel.html", name="World")

@app.route('/rgb_gavin/')
def rgb_gavin():
    return render_template('rgb_gavin.html', images=image_data())

if __name__ == "__main__":
    app.run(debug=True)