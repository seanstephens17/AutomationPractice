from flask import Flask, redirect, url_for, render_template
# video link https://www.youtube.com/watch?v=mqhxxeeTbu0&t=142s
app = Flask(__name__)  # instance of a flask web app


@app.route("/<name>")  # how to access this page
def home(name):  # defining home page
    return render_template("index.html", content=["tim", "joe", "bill"])  # can put html in here


if __name__ == "__main__":  # run the app
    app.run()

