from flask import Flask, render_template, request
from crossword import CrosswordApp
import datetime
app = Flask(__name__)
crosswordApp = CrosswordApp()


@app.route("/")
def home():
    return render_template("main.html")


@app.route("/explain")
def explain():
    return render_template("explain.html")


@app.route("/answers", methods=["POST"])
def answers():
    if len(request.form["clue"]) == 0:
        message = "Please enter a word!"
        return render_template("answers.html", msg=message, clues=[])
    possible_answers = crosswordApp.check_crossword('words_and_nouns.txt', request.form["clue"])
    message = "This is what we found"

    if len(possible_answers) == 0:
        message = "Sorry, no matching words"
        return render_template("answers.html", msg=message, clues=[])
    if len(possible_answers) > 85:
        possible_answers = []
        message = "There are too many words!"
    return render_template("answers.html", msg=message, clues=possible_answers)


if __name__ == "__main__":
    app.run(debug=True)

