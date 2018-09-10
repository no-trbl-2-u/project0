from app import app, db
from flask import render_template, request, jsonify
from models import Member
from help_func import apology, eprint


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

        # ======= Form Data =======
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")

        # ======= Database Interactions ======

        # TODO -> Hash password

        # Create placeholder for entire db of registrants
        rows = Member.query.all()

        # Instantiate a member with the properties from the Form Data
        registrant = Member(username=username, password=password, email=email)

        # Last line of defense against duplicate entries
        for row in rows:
            if username == row.username:
                return render_template("index.html")

        # All validation has been completed by this point

        # Commit registrant to database
        db.session.add(registrant)
        db.session.commit()

        return render_template("index.html")


@app.route("/register/validate", methods=['GET', 'POST'])
def register_validate():
    ''' Response to the XMLHttpRequest from JS '''

    if request.method == 'POST':

        # All the data relevant to a db check
        username = request.form['username']
        rows = Member.query.all()

        # Iterate through database to see if username present
        for row in rows:
            if username == row.username:
                return jsonify(isValid=False)

        return jsonify(isValid=True)
