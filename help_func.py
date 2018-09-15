from __future__ import print_function
import sys

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"),
                         ("?", "~q"), ("%", "~p"), ("#", "~h"),
                         ("/", "~s"), (" \" ", "''")]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message))


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def rem_Duplicate(duplicate):
    results = []
    for item in duplicate:
        if item not in results:
            results.append(item)
    return results


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
