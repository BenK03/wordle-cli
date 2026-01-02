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
    pass

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