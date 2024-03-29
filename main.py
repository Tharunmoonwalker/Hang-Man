import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_table(dictionary):
    print("{:<15} {:<10}".format("Key", "Value"))
    print("-" * 25)
    for key, value in dictionary.items():
        print("{:<15} {:<10}".format(key, value))


from hangman_words import word_list

score = {}
while True:
    intro = int(
        input("""
    PRESS 1 TO PLAY
    PRESS 2 FOR EXIT
    PRESS 3 FOR RESET
    """))
    if intro == 1:
        print(f"the leaderboard is {score}")
        chosen_word = random.choice(word_list)
        word_length = len(chosen_word)

        end_of_game = False
        lives = 6

        from hangman_art import logo

        print(logo)

        display = []
        for _ in range(word_length):
            display += "_"

        while not end_of_game:
            guess = input("Guess a letter: ").lower()

            if guess in display:
                print(f"You've already guessed {guess}")

            for position in range(word_length):
                letter = chosen_word[position]

                if letter == guess:
                    display[position] = letter

            if guess not in chosen_word:

                print(
                    f"You guessed {guess}, that's not in the word. You lose a life."
                )

                lives -= 1
                if lives == 0:
                    end_of_game = True
                    print(f"You lose.the solution is {chosen_word}")

            print(f"{' '.join(display)}")

            def update_score(score, key):
                if key in score:
                    score[key] += 1
                else:
                    score[key] = 1

            if "_" not in display:
                end_of_game = True
                print("You win.")
                name = input("Enter your name: ")
                update_score(score, name)
                clear_screen()
                print_table(score)

            from hangman_art import stages
            print(stages[lives])

    elif intro == 2:
        break
    elif intro == 3:
        score = {}
    else:
        print("Enter the valid option!!!")
