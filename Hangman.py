import random
from assets import clear

language = ""
guessed_characters = set()
possible_characters = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
wrong_guesses = 0
won = False
winning_streak = 0
gallows = [
    "\n\n\n\n\n\n\n",
    "\n\n\n\n\n\n\n________ ",
    "\n|\n|\n|\n|\n|\n|________ ",
    " ________\n|\n|\n|\n|\n|\n|________ ",
    " ________\n|    |\n|\n|\n|\n|\n|________ ",
    " ________\n|    |\n|    o\n|   /|\\\n|    |\n|   / \\\n|________ ",
    ]

def replayGame():
    clear()
    global guessed_characters,wrong_guesses,won,word
    guessed_characters.clear()
    wrong_guesses = 0
    won = False
    word = random.choice(wordlist)

def guessCharacter():
    while not won:
        guess = input(messages.guess_character)
        if guess == "lemmewin":
            for letters in possible_characters:   
                guessed_characters.add(letters)
        elif guess not in possible_characters:
            message = input(guess + messages.invalid_character)
        elif guess in guessed_characters:
            message = input(guess + messages.repeated_character)
        else:
            guessed_characters.add(guess)
            if guess not in word:
                global wrong_guesses
                wrong_guesses += 1
        break

def progress():
    progress = ""
    for letter in word:
        if letter in guessed_characters:
            progress += letter + " "
        else: 
            progress += "_ "
    if not "_" in progress:
        global won
        won = True
    print(progress)
    

def printGuessedCharacters():
    if len(guessed_characters):
        print(messages.guessed_characters + ', '.join(guessed_characters))
    else:
        print("\n")

clear()
while not language == "nl" and not language == "en":
    language = input("Which language do you want to play in? (nl|en) ")
    if language == "en":
        from assets import english_wordlist as wordlist
        from assets import english_messages as messages
    else:
        from assets import dutch_wordlist as wordlist
        from assets import dutch_messages as messages

    word = random.choice(wordlist)

while True:
    clear()
    if wrong_guesses == 5:
        print(gallows[wrong_guesses])
        print(messages.lose + word)
        if winning_streak > 0:
            print(messages.winning_streak + str(winning_streak))
        winning_streak = 0
    elif won:
        print(gallows[wrong_guesses])
        winning_streak += 1
        print(messages.win + word + ". " + messages.winning_streak + str(winning_streak))

    if wrong_guesses == 5 or won:
        replay = input(messages.replay)
        if replay == "y":
            replayGame()
        else:
            break
    print(gallows[wrong_guesses])
    printGuessedCharacters()
    progress()
    guessCharacter()