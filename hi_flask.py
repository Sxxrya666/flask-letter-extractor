from flask import Flask, render_template, request
from firstmodule import search4letters

app = Flask(__name__)


@app.route("/")
def hello_world() -> str: 
    return "hello world!! first first time running flask!"


@app.route("/entry", methods=['GET', 'POST'])
def entry():
    return render_template("entry.html", the_title="Welcome to search for letters!! | this is title")


@app.route("/converted-results", methods=["GET" , "POST"])
def do_search() -> str:
    phrase = request.form["phrase"]
    print(phrase)
    letters = request.form["letters"]
    print(letters)
    title = 'Here are your results:' 
    results = str(search4letters(phrase, letters))
    return render_template("results.html", the_title=title, the_phrase=phrase, the_letters=letters, the_results=results)


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)