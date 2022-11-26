from flask import Flask, render_template, request, make_response

app = Flask(__name__)

USER_VALIDATION = False

# username validation
def user_validation(userName):
    if userName == "" or userName == None:
        return make_response(render_template("error.html"))
    else:
        global USER_VALIDATION
        USER_VALIDATION = True


#login page sets cookie with username  
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        userName = request.form['username']
        # username validation
        user_validation(userName)
        print(USER_VALIDATION)
    if USER_VALIDATION == False:
        return make_response(render_template("error.html"))
    else:
        resp = make_response(render_template("success.html"))
        resp.set_cookie('username', userName)
    return resp


# home page
@app.route('/home')
def profile():
    userName = request.cookies.get('username')  
    # username validation
    print(USER_VALIDATION)
    if USER_VALIDATION == False:
        return make_response(render_template("error.html"))
    else:
        return render_template('home.html', name=userName)


#login page 
@app.route('/')
def login():
   return render_template('login.html')


# list storing current characters
characters = [
    "Albert",
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
    "Chad",
    "all"
]


# route to approprate character page
@app.route("/characters/<name>")
def generic(name):
    for character in characters:
        if name == character.lower():
            site = f"/characters/{name}.html"
            return render_template(site)
    else:
        return "That character does not exist"


@app.route("/how-to")
def how_to():
    return render_template("how-to.html")


# custom 404
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


# main
if __name__ == "__main__":
	app.run()
