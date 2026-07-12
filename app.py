from flask import Flask, render_template, session

from auth.login import login_bp
from auth.register import register_bp

app = Flask(__name__)

app.secret_key = "movie_theatre_secret_key"

app.register_blueprint(login_bp)
app.register_blueprint(register_bp)


@app.route("/theatre")
def theatre():

    return render_template(
        "theatre.html",
        firstname=session.get("firstname"),
        lastname=session.get("lastname"),
        movie=session.get("movie")
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
