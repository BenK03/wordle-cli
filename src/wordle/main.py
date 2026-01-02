import argparse
import random

# puts all words into an array
def load_words():
    words = []
    with open("data/words.txt", "r", encoding="utf-8") as file:
        for line in file:
            line.strip()
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

        elif guess == target_word:
            #temp (add play again after and green colouring)
            print("Congrats, you got it!")
            return
        
        else:
            # guess is valid but not target
            # add green colouring
            evaluate_guess(guess, target_word)
            
        guesses_left -= 1

    # temp (add play again after)
    print("Game over")

# controls commands
def main():
    parser = argparse.ArgumentParser(description="Wordle game")
    
    # add an argument --start
    parser.add_argument( "--start", action="store_true", help="Start a new Wordle game")

    # store command in variable
    args = parser.parse_args()

    # test
    if args.start:
        start_game()


if __name__ == "__main__":
    main()