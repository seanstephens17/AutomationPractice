from flask import Flask, redirect, url_for, render_template
# video link https://www.youtube.com/watch?v=mqhxxeeTbu0&t=142s
app = Flask(__name__)  # instance of a flask web app


@app.route("/")  # how to access this page
def home():  # defining home page
    return "Hello, this is the main page <h1>Hello<h1>"  # can put html in here


@app.route("/<name>")  # pass in as a parameter to return value below e.g. could be used to get a post ID
def user(name):
    return f"Hello {name}!"


@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))  # name of function you want to move to if unauthorized


if __name__ == "__main__":  # run the app
    app.run()

