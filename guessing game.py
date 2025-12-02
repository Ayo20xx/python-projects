import random

def guessing():
    num_1 = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20...")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number!")
            continue

        if guess == num_1:
            print("🎉 Correct! You guessed it!")
            break
        elif guess < num_1:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    again = input("Do you want to play again? (yes/no): ").strip().lower()
    if again == "yes":
        guessing()
    else:
        print("Goodbye 👋🏽")

start = input("Welcome to the guessing game! Press 's' to start: ").strip().lower()
if start == "s":
    guessing()
else:
    print("Goodbye!")
