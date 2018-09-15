from app import app, db
from flask import render_template, request, jsonify, redirect, url_for, session
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from models import Member
from help_func import apology, eprint, login_required


@app.route("/")
@login_required
def index():

    if request.method == 'GET':
        firstmember = Member.query.first()
        return render_template('index.html', firstmember=firstmember.username)


@app.route("/login", methods=['GET', 'POST'])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username & password
        rows = Member.query.filter_by(username=username).all()
        db_pass = rows[0].password

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(db_pass, password):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0].id

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=['POST', 'GET'])
def register():
    """ Route to register a user """

    if request.method == 'GET':
        return render_template("register.html")

    if request.method == "POST":

        # ======= Form Data =======
        # Force lowercase for case insensitivity
        username_raw = request.form.get("username")
        username = username_raw.lower()

        # Hash password
        password_raw = request.form.get("password")
        password = generate_password_hash(password_raw)

        email = request.form.get("email")

        # ======= Database Interactions ======

        # Create Member object to store into database
        registrant = Member(username=username, password=password, email=email)

        # All validation has been completed by this point
        # Commit registrant to database
        db.session.add(registrant)
        db.session.commit()

        return render_template("index.html")


@app.route("/create_char", methods=['POST', 'GET'])
@login_required
def create_char():
    return render_template("create_char.html")


@app.route("/register/validate", methods=['GET', 'POST'])
def register_validate():
    ''' Response to the XMLHttpRequest from JS '''

    if request.method == 'GET':
        return redirect(url_for('register'))

    if request.method == 'POST':

        # All the data relevant to a db check
        username = request.form['username']
        rows = Member.query.all()

        # Iterate through database to see if username present
        for row in rows:
            if username == row.username:
                return jsonify(isValid=False)

        return jsonify(isValid=True)


@app.route("/index/updateModels", methods=['GET', 'POST'])
def updateModels():
    """ Index's Local AJAX call """
    if request.method == 'GET':
        db.drop_all()
        db.create_all()

        password = generate_password_hash("admin")

        registrant = Member(username="admin", password=password, email="@")

        db.session.add(registrant)
        db.session.commit()

        return redirect("/login")


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
