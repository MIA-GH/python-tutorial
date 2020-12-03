# # # number guesser
import random

# # # DRY == dont repeat yourself


def decide(guess, randomNumber):
    if guess == randomNumber:
        print("Congratulations, you got it right")
    elif guess > randomNumber:
        print("Guess Lower")
    else:
        print("Guess Higher")

# def brain(guess, randomNumber):
#     try:
#         guess = int(guess)
#         decide(guess, randomNumber)
#     except ValueError:
#         print("Invalid Input, Integers only")


def main():
    # generate random number
    randomNumber = random.randint(1, 20)
    guess = input("Make a guess between 1 and 20 >> ")
    print(randomNumber)
    try:
        guess = int(guess)
        decide(guess, randomNumber)
    except ValueError:
        print("Invalid Input, Integers only")

    # if guess == randomNumber:
    #     print("Congratulations, you got it right")
    # elif guess > randomNumber:
    #     print("Guess Lower")
    # else:
    #     print("Guess Higher")

    while guess != randomNumber:
        guess = input("Make a guess between 1 and 20 >> ")
        try:
            guess = int(guess)
            decide(guess, randomNumber)
        except ValueError:
            print("Invalid Input, Integers only")

        # if guess == randomNumber:
        #     print("Congratulations, you got it right")
        # elif guess > randomNumber:
        #     print("Guess Lower")
        # else:
        #     print("Guess Higher")


if __name__ == "__main__":
    main()
