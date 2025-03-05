import pytest
from flask import Flask, session
from project import get_random_word, start_new_game, load_words

app = Flask(__name__)
app.secret_key = "secretkey"  # Required for session handling


def test_load_words():
    words = load_words()
    assert isinstance(words, list)
    assert len(words) > 0


def test_get_random_word():
    word = get_random_word()
    assert isinstance(word, str)
    assert word.isupper()


def test_start_new_game():
    with app.test_request_context():  # Provide Flask request context
        start_new_game()
        assert isinstance(session["word"], str)
        assert session["word"].isupper()
        assert session["attempts"] == 5
