from flask import Flask

app = Flask(__name__)

app.secret_key = "movie_theatre_secret_key"

@app.route("/")
def home():
    return """
    <h1>🎬 Movie Theatre Application</h1>
    <h3>Application is Running Successfully!</h3>
    <p>Login and Registration pages will be added in the next step.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
