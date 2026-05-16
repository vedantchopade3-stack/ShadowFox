import random

# Multiple words with hints
word_list = {
    "python": "Programming language",
    "computer": "Electronic machine",
    "elephant": "Largest land animal",
    "football": "Popular sport",
    "hospital": "Medical place",
    "keyboard": "Typing device",
    "internet": "Global network",
    "airplane": "Flying vehicle",
    "mountain": "Very high landform",
    "notebook": "Used for writing",
    "chocolate": "Sweet food item",
    "astronaut": "Person who travels to space",
    "telescope": "Used to see distant objects",
    "university": "Higher education place",
    "diamond": "Precious stone",
    "microscope": "Scientific instrument",
    "engineer": "Designs and builds things",
    "calculator": "Used for calculations",
    "restaurant": "Place to eat food"
}

hangman = [
'''
 -----
 |   |
 |
 |
 |
 |
=========
''',
'''
 -----
 |   |
 |   O
 |
 |
 |
=========
''',
'''
 -----
 |   |
 |   O
 |   |
 |
 |
=========
''',
'''
 -----
 |   |
 |   O
 |  /|
 |
 |
=========
''',
'''
 -----
 |   |
 |   O
 |  /|\\
 |
 |
=========
''',
'''
 -----
 |   |
 |   O
 |  /|\\
 |  /
 |
=========
''',
'''
 -----
 |   |
 |   O
 |  /|\\
 |  / \\
 |
=========
'''
]


def play_game():

    # Random word every game
    word = random.choice(list(word_list.keys()))
    hint = word_list[word]

    guessed = []
    wrong = 0
    max_attempts = 6

    print("\n====== HANGMAN ======")
    print("Hint:", hint)

    while True:

        print(hangman[wrong])

        display = ""

        for letter in word:

            if letter in guessed:
                display += letter + " "

            else:
                display += "_ "

        print("Word:", display)
        print("Guessed:", guessed)
        print("Remaining attempts:",
              max_attempts-wrong)

        # Win
        if "_" not in display:
            print("\n🎉 Congratulations!")
            print("You guessed:", word)
            break

        # Lose
        if wrong >= max_attempts:
            print("\n Game Over")
            print("Correct word:", word)
            break

        guess = input(
            "\nGuess a letter: "
        ).lower()

        # Input validation
        if len(guess) != 1 \
           or not guess.isalpha():

            print("Enter only one letter")
            continue

        if guess in guessed:
            print("Already guessed")
            continue

        guessed.append(guess)

        if guess not in word:
            wrong += 1
            print("Wrong Guess!")

while True:

    play_game()

    again = input(
        "\nPlay Again? (yes/no): "
    ).lower()

    if again != "yes":
        print("Thanks for playing!")
        break