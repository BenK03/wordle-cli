import argparse
import random
from importlib import resources

# constants
GREEN = "\033[1;42m"
YELLOW = "\033[1;43m"
GRAY = "\033[1;100m"
RESET = "\033[0m"

GAME_RULES = """
Wordle (Terminal Version)

Rules:
- Guess the hidden 5-letter word in 6 attempts.
- Each guess must be a valid 5-letter word.
- After each guess, letters are colored:
  Green  : correct letter in the correct position
  Yellow : correct letter in the wrong position
  Gray   : letter not in the word
- You win by guessing the word within 6 tries.
"""

# puts all words into an array
def load_words():
    words = []
    with resources.files("wordle").joinpath("data/words.txt").open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line:
                words.append(line)
    return words

# finds feedback for each letter
def evaluate_guess(guess, target_word):
    feedback = ["gray"] * 5
    target_word_array = list(target_word)

    # check greens
    for i in range(5):
        if guess[i] == target_word_array[i]:
            feedback[i] = "green"
            # covers duplicates
            target_word_array[i] = None
        
    # check yellows
    for i in range(5):
        if feedback[i] == "gray" and guess[i] in target_word_array:
            feedback[i] = "yellow"
            # covers duplicates
            target_word_array[target_word_array.index(guess[i])] = None

    return feedback

def render_colours(guess, feedback):
    output = ""

    for i in range(5):
        if feedback[i] == "green":
            colour = GREEN

        elif feedback[i] == "yellow":
            colour = YELLOW

        else:
            colour = GRAY

        output += f"{colour} {guess[i].upper()} {RESET}"

    # testing
    print(output)

# play again function
def play_again():
    ans = input("Play again? (y/n): ").strip().lower()

    if ans != "y" and ans != "n":
        print("Invalid input. Please enter y or n.")
        return play_again()

    if ans == "y":
        return True
    
    return False

# game logic/start game
def start_game():
    words = load_words()
    target_word = random.choice(words)

    guesses_left = 6

    while guesses_left > 0:
        guess = input("Enter a 5 letter word: ").strip().lower()

        if len(guess) != 5:
            print("Invalid guess. Only 5 letter words.")
            continue
            
        elif not guess.isalpha():
            print("Invalid guess. Only letters.")
            continue

        feedback = evaluate_guess(guess, target_word)
        render_colours(guess, feedback)

        if guess == target_word:
            print("Congrats, you got it!")
            ans = play_again()

            if ans:
                return start_game()
            return
            
        guesses_left -= 1

    print("Game over")
    ans = play_again()
    if ans:
        return start_game()
    return

    


# controls commands
def main():
    parser = argparse.ArgumentParser(description="Wordle game", epilog=GAME_RULES, formatter_class=argparse.RawDescriptionHelpFormatter)
    
    # add an argument --start
    parser.add_argument( "--start", action="store_true", help="Start a new Wordle game")

    # store command in variable
    args = parser.parse_args()

    # test
    if args.start:
        start_game()


if __name__ == "__main__":
    main()