# import "packages" from flask
from flask import Flask, render_template, request
from image import image_data
import requests
import json
# create a Flask instance
app = Flask(__name__)
from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

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
            return render_template("gavin.html", name=name)
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

@app.route('/rgb/')
def rgb():
    path = Path(app.root_path) / "static" / "assets"
    return render_template('rgb.html', images=image_data(path))

@app.route('/logicgatess/')
def logicgatess():
    return render_template("logicgatess.html")

@app.route('/ColorCodes/')
def colorcodes():
    return render_template("ColorCodes.html")
@app.route('/binary_addition/', methods=['GET', 'POST'])
def unsigned():
    return render_template("binary_addition.html", BITS=8, imageOn="/static/assets/bulb_on2.PNG", imageOff="/static/assets/bulb_off2.PNG")

@app.route('/signed/', methods=['GET', 'POST'])
def signed():
    return render_template("signed.html", BITS=8, imageOn="/static/assets/bulb_on2.PNG", imageOff="/static/assets/bulb_off2.PNG")
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/topics/')
def topics():
    return render_template("topics.html")

@app.route('/study/',methods=['GET','POST'])
def study():
    url = "https://trivia-by-api-ninjas.p.rapidapi.com/v1/trivia"
    headers = {
        'x-rapidapi-host': "trivia-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': "6279ac9b7amsh7dc015c7d7746fbp1f4d65jsn125b0c500438"
    }
    response = requests.request("GET", url, headers=headers)
    output = json.loads(response.text)
    return render_template('study.html', question=output)
@app.route('/quiz/',methods=['GET','POST'])
def quiz():
    url = "https://trivia-by-api-ninjas.p.rapidapi.com/v1/trivia"
    headers = {
        'x-rapidapi-host': "trivia-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': "6279ac9b7amsh7dc015c7d7746fbp1f4d65jsn125b0c500438"
    }
    response = requests.request("GET", url, headers=headers)
    output = json.loads(response.text)
    mode=request.args.get('mode')
    topic=request.args.get('topic')

    return render_template("quiz.html", question=output,mode=mode)
@app.route('/test/')
def test():
    source = request.args.get('source')
    return render_template("test.html", source = source)

@app.route('/start/')
def start():
    return render_template("start.html")
topics = []
if __name__ == "__main__":
    app.run(debug=True)

