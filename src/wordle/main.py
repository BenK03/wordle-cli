import argparse
import random

def load_words():
    words = []
    with open("data/words.txt", "r", encoding="utf-8") as file:
        for line in file:
            line.strip()
            words.append(line)
    
    return words

def start_game():
    words = load_words()
    target_word = random.choice(words)

    guesses_left = 6

    while guesses_left > 0:
        guess = input("Enter a 5 letter word: ").strip().lower()

        if len(guess) != 5:
            print("Invalid guess. Only 5 letter words.")
            continue
            
        if not guess.isalpha():
            print("Invalid guess. Only letters.")
            continue

        if guess == target_word:
            #temp (add play again after)
            print("Congrats, you got it!")
            return

        guesses_left -= 1

    # temp (add play again after)
    print("Game over")

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