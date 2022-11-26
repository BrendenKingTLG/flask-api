from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        userName = request.form['username']
        if userName == "" or userName == None:
            return make_response(render_template("error.html"))
    resp = make_response(render_template("success.html"))
    resp.set_cookie('username', userName)
    return resp

@app.route('/profile')
def profile():
    userName = request.cookies.get('username')  
    if userName == None or userName == "":
        return make_response(render_template("error.html"))
    return render_template('profile.html', name=userName)

@app.route('/')
def login():
   return render_template('login.html')

characters = [
    "Anthony",
    "Brenden",
    "Craig",
    "Deja",
    "Elihu",
    "Eric",
    "Giovanni",
    "James",
    "Joshua",
    "Maria",
    "Mohamed",
    "PJ",
    "Philip",
    "Sagan",
    "Suchit",
    "Mieka",
    "Trey",
    "Winton",
    "Xiuxiang",
    "Yaping",
    "Chad"
]
@app.route("/characters/")
def all():
    return render_template("/characters.html")


@app.route("/characters/<name>")
def generic(name):
    for character in characters:
        if name == character.lower():
            site = f"/characters/{name}.html"
            return render_template(site)
    else:
        return "That character does not exist"

if __name__ == "__main__":
	app.run()
