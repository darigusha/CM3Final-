import random
import os
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "secretkey"  # Needed for session storage


# Load words from a file
def load_words():
    file_path = os.path.join(os.path.dirname(__file__), "words.txt")
    with open(file_path) as f:
        words = f.read().splitlines()
    return words


# Select a random word
def get_random_word():
    words = load_words()
    return random.choice(words).upper()


# Initialize a new game
def start_new_game():
    session["word"] = get_random_word()
    session["guessed"] = []
    session["attempts"] = 5


@app.route("/", methods=["GET", "POST"])
def index():
    if "word" not in session:
        start_new_game()

    word = session["word"]
    guessed = session.get("guessed", [])
    attempts = session.get("attempts", 5)

    if request.method == "POST":
        letter = request.form["letter"].upper()
        if letter not in guessed:
            guessed.append(letter)
            if letter not in word:
                session["attempts"] -= 1

        session["guessed"] = guessed
        attempts = session["attempts"]

    # Generate display word
    display_word = " ".join([letter if letter in guessed else "_" for letter in word])

    game_over = attempts == 0 or "_" not in display_word

    return render_template(
        "index.html",
        word=display_word,
        guessed=guessed,
        attempts=attempts,
        game_over=game_over,
        actual_word=word,
    )


@app.route("/reset", methods=["GET", "POST"])
def reset():
    start_new_game()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
