import random
import string


def play_game():

    choice = "Y"
    while choice == "Y":
        word_list = ["HANGMAN", "CAR", "BIKE"]

        random_word = random.choice(word_list)

        random_word_letters = set(random_word)

        guessed_word = set()

        alphabet = set(string.ascii_uppercase)

        life = 8
        
        while life > 0 and len(random_word_letters) > 0:
            print(f"Live Remaining: {life}")
            print(f"You Guessed: {' '.join(guessed_word)}")

            remaining_word = [letter if letter in guessed_word else '_' for letter in random_word]
            print(f"Current Word: {' '.join(remaining_word)}")

            player_input = input("Insert your guess here:").upper()
            if player_input in alphabet - guessed_word:
                guessed_word.add(player_input)
                if player_input in random_word:
                    random_word_letters.remove(player_input)
                else:
                    life = life - 1
                    print(f"Sike, {player_input} is a wrong guess. Try Again")
            else:
                print(f"{player_input} is not a valid guess. Please try again.")
                print("Make sure you inserted A letter without any spaces.")

        if life == 0:
            print(f"Live Remaining: {life}")
            print("You have lost the game.")
            print(f"Word: {random_word}")
            choice = input("Play Again?(Y/N):").upper()

        else:
            print(f"You WIN! You guessed {random_word} !")
            choice = input("Play Again?(Y/N):").upper()

    

play_game()

        

    