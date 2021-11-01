# import "packages" from flask
from flask import Flask, render_template, request
from image import image_data
import requests
import json
# create a Flask instance
app = Flask(__name__)
from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
import random
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

@app.route('/modes/')
def start():
    topic = [
        {"topic": "Animal Trivia","Description":"Can you guess the animals?","image1":"/static/assets/silhouette-animal-clipart-11.jpg"},
        {"topic": "Movie Trivia","Description":"Match famous movie quotes with your favorite movies","image1":"/static/assets/Movie.png"},
        {"topic": "Geography Trivia","Description":"Test your geography knowledge with this trivia","image1":"../static/assets/Globe.JPG"},
        {"topic": "America Trivia","Description":"Test what you know about America, including historical events and laws","image1":"/static/assets/AmericanFlag.jfif"},
        {"topic": "Planet Trivia","Description":"What do you know about the planets in our solar system?","image1":"../static/assets/SaturnSilhoutte.png"},
        {"topic": "Food Trivia","Description":"See if you know where these popular food items originated from","image1":"/static/assets/Fastfood.JPG"}
    ]
    modes = [
        {'name':'Single Question','param':'Single-Q','Description':"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean at metus sed est imperdiet suscipit. Nam semper nulla vitae diam rhoncus feugiat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed at metus euismod orci dictum congue. Nulla eget lectus faucibus, feugiat leo vel, dapibus arcu. "},
        {'name':'Test','param':'test','Description':"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean at metus sed est imperdiet suscipit. Nam semper nulla vitae diam rhoncus feugiat. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed at metus euismod orci dictum congue. Nulla eget lectus faucibus, feugiat leo vel, dapibus arcu. "}
    ]
    return render_template("modes.html", topics=topic,modes=modes)

@app.route('/study_general/',methods=['GET','POST'])
def study_general():
    url = "https://trivia-by-api-ninjas.p.rapidapi.com/v1/trivia"
    headers = {
        'x-rapidapi-host': "trivia-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': "6279ac9b7amsh7dc015c7d7746fbp1f4d65jsn125b0c500438"
    }
    response = requests.request("GET", url, headers=headers)
    output = json.loads(response.text)
    return render_template('study_general.html', question=output)


@app.route('/instructions/')
def instructions():
    return render_template("instructions.html")

@app.route('/movieapi/')
def movieapi():
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    querystring = {"r":"json","type":"movie","i":"tt{id}".format(id=random.randint(1000000,4000000))}

    headers = {
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
        'x-rapidapi-key': "7815f70232mshea0c87cc336b4aap13f459jsn464272722115"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    return render_template("movieapi.html", moviequiz=data)

@app.route('/quiz/',methods=['GET','POST'])
def quiz():
    possible_topics = {
        'history':'historyholidays',
        'food':'fooddrink',
        'language':'language',
        'science':'sciencenature',
        'geography':'geography',
        'religion':'religionmythology',
        'sports':'sportsleisure'
    }
    topic = request.args.get('topic')
    if topic == "math":
        url = "https://numbersapi.p.rapidapi.com/{num}/trivia".format(num=random.randint(0,40))
        querystring = {"fragment":"v8","notfound":"floor","json":"true"}
        headers = {
            'x-rapidapi-host': "numbersapi.p.rapidapi.com",
            'x-rapidapi-key': "a217c5e6c1msh46f25df6216c5aap19e736jsn947379489fc9"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        output = json.loads(response.text)
        selectors = ['text','number']
    elif topic in list(possible_topics.keys()):
        url = "https://trivia-by-api-ninjas.p.rapidapi.com/v1/trivia"
        querystring = {"category":possible_topics[topic.lower()]}
        headers = {
            'x-rapidapi-host': "trivia-by-api-ninjas.p.rapidapi.com",
            'x-rapidapi-key': "6279ac9b7amsh7dc015c7d7746fbp1f4d65jsn125b0c500438"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        output = json.loads(response.text)[0]
        selectors=['question','answer']
    else:
        url = "https://trivia-by-api-ninjas.p.rapidapi.com/v1/trivia"
        headers = {
            'x-rapidapi-host': "trivia-by-api-ninjas.p.rapidapi.com",
            'x-rapidapi-key': "6279ac9b7amsh7dc015c7d7746fbp1f4d65jsn125b0c500438"
        }
        response = requests.request("GET", url, headers=headers)
        output=json.loads(response.text)[0]
        selectors=['question','answer']
    mode='Single-Q'
    if request.form:
        mode = request.form['mode']
    return render_template("quiz.html", question=output, selectors=selectors,topic=topic,mode=mode)

@app.route('/gaem/')
def gaem():
    return render_template("gaem.html")

@app.route('/mathtrivia/',methods=['GET', 'POST'])
def mathtrivia():
    userInput= 0
    if request.method == 'POST':
        userInput = int(request.form['userInput'])
    url = "https://numbersapi.p.rapidapi.com/{num}/trivia".format(num=int(userInput))
    querystring = {"fragment":"v8","notfound":"floor","json":"true"}
    headers = {
    'x-rapidapi-host': "numbersapi.p.rapidapi.com",
    'x-rapidapi-key': "a217c5e6c1msh46f25df6216c5aap19e736jsn947379489fc9"
}
    response = requests.request("GET", url, headers=headers, params=querystring)
    output = json.loads(response.text)
    return render_template("mathtrivia.html", trivia=output, userInput=userInput)


if __name__ == "__main__":
    app.run(debug=True)