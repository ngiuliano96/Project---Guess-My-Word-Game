import random

# List of potential words to choose from (10 nouns, 10 verbs, and 10 adjectives)
word_set = ["quarter", "industry", "drain", "loaf", "neck", "condition", "mom", "letter", "low", "place", "tip", "disappear", "start", "untidy", "correct", "provide", "seal", "switch", "scare", "recognise", "cross", "poke", "enthusiastic", "nutritious", "draconian", "direful", "panoramic", "military", "silly", "lean", "educated", "majestic", "sore", "future"]

# Choose a random word from the words list
random.shuffle(word_set)
random_word = random.choice(word_set)

# Split the random word into a list of its characters and create a list of asterisks of the same length
word_characters = list(random_word)
mystery_list = ["*"] * len(word_characters)

# Greet player and explain game
print("Welcome to Guess My Word, the game where you have 6 chances to figure out the mystery word. You can guess one letter at a time, or guess the whole word!" )

# Initiate while loop to allow player to guess while they have lives left
lives = 6
while lives > 0:
    # Main conditional block for player guessing and game checking matches
    guess_choice = input("Type 1 to guess a letter or 2 to guess the whole word:\n")
    guess_match = False
    if guess_choice == "1":
        guess_letter = input("Type the letter you want to guess:\n").lower()
        
        # Run through word list and check for guess matches
        count = 0
        for character in word_characters:
            if guess_letter == character:
                mystery_list[count] = character
                guess_match = True
            count += 1

        # Check if player guessed a letter or not
        if(guess_match == True):
            print(f'You guessed a letter:\n{" ".join(mystery_list)}')
        else:
            lives -= 1
            print(f"Wrong guess! You have {lives} lives left.")
        
        # Check if the player guessed the whole word
        if ("".join(mystery_list)) == random_word:
            print(f"Congratulations, you guessed the whole word: {random_word}")
            lives = -1
            
    elif guess_choice == "2":
        guess_word = input("Type the word you want to guess:\n").lower()
        
        # Check if the player guessed the word
        if guess_word == random_word:
            print(f"Congratulations, you guessed the word: {random_word}")
            lives = -1
        else:
            lives -= 1
            print(f"Wrong guess! You have {lives} lives left.")
    else:
        print("Invalid choice. You have to type 1 or 2!")
    
    # Conditional block to check if no lives are left
    if lives == 0:
        print("You've ran out of lives. Game over!")
