from app import app, db
from flask import render_template, request, jsonify
from models import Member
from help_func import apology, eprint

username_not_in_db = False


@app.route("/")
def index():

    firstmember = Member.query.first()

    return render_template('index.html', firstmember=firstmember.username)


@app.route("/javascript")
def javascript():
    return render_template("javascript.html")


@app.route("/register", methods=['POST', 'GET'])
def register():
    """ Route to register a user """

    if request.method == 'GET':
        if request.method == 'GET':
            return render_template('register.html')
        return jsonify(['test', 'test2'])

    if request.method == "POST":

        # ======= User Name =======
        if request.form.get("username") is not "":
            username = request.form.get("username")
        else:
            return apology("Please Enter a Username", 403)

        # ======= Pass Word =======
        if request.form.get("password") is not "":
            password = request.form.get("password")
        # TODO -> Hash password
        else:
            return apology("Empty Password Field", 407)

        # ======== Email =======
        if request.form.get("email") is not "":
            email = request.form.get("email")

        # ======== Is Verified? =======
        isValid = False

        # ======= Database ======
        # Continue to fine tune the input
        # TODO -> Hash password
        rows = Member.query.all()
        registrant = Member(username=username, password=password, email=email)

        # for row in rows:
        #     if username == row.username:
        #         return render_template("index.html")
        #     else:
        #         # db.session.add(registrant)
        #         # db.session.commit()

        return render_template("index.html", isValid=isValid)


@app.route("/register/validate", methods=['GET', 'POST'])
def register_validate():

    # EXPLAIN THE TRAILING WHITESPACE IN THE USERNAME RESPONSE!!
    if request.method == 'POST':
        username = request.form['username ']

        eprint(username)
        eprint(request.data)
        return jsonify("XHR complete")
        
    eprint("test")
    return render_template("index.html")
