import argparse

def main():
    parser = argparse.ArgumentParser(description="Wordle game")
    
    # add an argument --start
    parser.add_argument( "--start", action="store_true", help="Start a new Wordle game")

    # store command in variable
    args = parser.parse_args()

    # test
    if args.start:
        print("Game start requested")



if __name__ == "__main__":
    main()