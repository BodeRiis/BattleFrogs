# BattleFrogs is a React JSX based Battleship Game coded by
# github . com / BodeRiis
# using the 'Hunt (with Parity)/Target' algorithm described by Nick Berry here:
# www . datagenetics . com / blog / december32011 / 

from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    flash,
    redirect,
    session,
    abort,
    url_for,
    Request,
)

import os
import io

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.secret_key = 'thefriendswemadealongtheway'

###############

@app.route("/")
def battlefrogs():
    """Renders the one page app, BattleFrogs"""

    return render_template("battlefrogs.html")

###############

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    # db.app = app
    # db.init_app(app)
    # connect_to_db(app)
    toolbar = DebugToolbarExtension(app)
    # Use the DebugToolbar
    # DebugToolbarExtension(app)
    app.debug = True
    app.run(host="0.0.0.0")
