🎮 Hangman Game - Flask Web Application

https://youtu.be/wXFfHp4Qfqo?si=tbBBMiJx35Txl7CD


📌Overview
We created a Hangman Game! It is a web-based game coded using Python and Flask as a base and HTML for additional coding. The point of this game is that you have the hidden word and you need to guess the letter one-by-one to get the word. With every letter that is wrong, your number of attempts decreases. The available attempts at the start of the game are 5, so make sure that you think through your guesses. 


🔹 Features


✔ UI features  –Letters are formatted in buttons that change when you click on them


✔ Random Word Selection –500 words list that is randomly chosen from words.txt 


✔ 5 Attempts Limit –player has only 5 attempts to guess wrong letters 			


✔ Play Again Button – allows users to restart the game and play again	


✔ Win/Lose Messages – shows the result of the game 


✔ Mobile Responsive – this game is available on laptops, phones, and tablets 



📁 Structure 


bash


CopyEdit


/project


│── /static


│   ├── styles.css  # style code for the webpage 


│── /templates


│   ├── index.html  # Interface of the game 


│── project.py       # Main code for the game 


│── test_project.py  # Unit tests using pytest


│── requirements.txt # Dependencies for the project


│── words.txt        # List of words for the game


⚙️ Technologies Used


Python (Flask for the backend)


HTML (Game structure)


CSS (Styling and animations)


pytest (For unit testing)

🚀 Installation Guide


Follow these steps to set up and run the Hangman Game on your local machine.


1️⃣ Clone the Repository


bash


CopyEdit


git clone https://github.com/darigusha/CM3Final


cd project.py



2️⃣ Create a Virtual Environment (Optional)


It’s best practice to use a virtual environment:


bash


CopyEdit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies
bash
CopyEdit
pip install -r requirements.txt

4️⃣ Run the Application
bash
CopyEdit
python project.py

Open http://127.0.0.1:5000/ in your browser to play the game.

🖥️ How the Game Works


From the file words.txt one word will be selected.


This word is displayed as (_), meaning that the letters are blank yet.


The player clicks a letter:


✅ Correct letters → Displays on the _ that corresponds to the letter and turns green 


❌ Incorrect letters → Decrease one attempt and turn red 


The game ends when:
The player guesses the word correctly → "Congratulations! You guessed the word!"


The player runs out of attempts → "Game Over! The word was XYZ"


The Play Again button resets the game with a new random word.



📜 Code Explanation


1️⃣ project.py (Main Backend)


Flask App Setup → Initializes the Flask application and session handling.


load_words() → Loads words from words.txt.


get_random_word() → Selects a random word from the list.


start_new_game() → Resets the game state (new word, resets attempts).


index() Route → Handles game logic, checking guesses, and rendering UI.


reset() Route → Resets the game when the "Play Again" button is clicked.


2️⃣ templates/index.html (Frontend UI)




Displays the hidden word using underscores.


Creates clickable letter buttons.


Shows attempts left.


Includes the "Play Again" button.



3️⃣ static/styles.css (UI Design)


Bigger buttons for better usability.


Correct letters turn green and incorrect letters turn red 


Brown letters and pink background 


Hover effects & animations for an interactive experience.


Responsive design so the game works on all screen sizes.


4️⃣ test_project.py (Unit Tests)


test_load_words() → Checks if words are loaded correctly.


test_get_random_word() → Ensures a word is randomly selected.


test_start_new_game() → Verifies the game state resets correctly.




🧪 Running Tests

To ensure everything works correctly, run:
bash
CopyEdit
pytest

If successful, it will show:
diff
CopyEdit
=================== 3 passed in 0.10s ===================


📌 Future Enhancements



🔹 Add a Leaderboard to track high scores


🔹 Add a Hint Button to reveal one letter


🔹 Add Different Difficulty Levels (Easy, Medium, Hard)


🔹 Add Sound Effects when clicking letters



💡 Lessons Learned


How to build a Flask web application.


How to handle user interaction with Flask sessions.


How to create a responsive UI using CSS.


How to write unit tests for a Flask app.


How to manage game state with Python functions.




💻 Author


👤 Dariga Bazhanova, Meryem Annaberdiyeva


📧 Contact: bazhanovadariga0@gmail.com


🌎 GitHub: darigusha, Meryem-code




📝 License


This project is open-source and available under the MIT License. Feel free to modify and use it! 🚀

We used Chat GPT as assistant to perform debugging, code checks, and help with overall questions. 



🎉 Thank you for checking out this project! Have fun playing Hangman! 🎮🔥

We used Chat GPT as assistant to perform debugging, code checks, and help with overall questions. 
