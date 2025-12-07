import random

def play_game():
    lower_bound = 1
    upper_bound = 100

    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    print("🎯 Welcome to Guess the Number game!")
    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}. Try to guess it!")

    while True:
        try:
            guess = int(input(f"Enter your guess ({lower_bound}–{upper_bound}): "))
        except ValueError:
            print("❗ Invalid input — please enter an integer.")
            continue

        if guess < lower_bound or guess > upper_bound:
            print(f"⚠️ Please guess a number between {lower_bound} and {upper_bound}.")
            continue

        attempts += 1

        if guess < secret_number:
            print("🔼 Too low! Try a higher number.")
        elif guess > secret_number:
            print("🔽 Too high! Try a lower number.")
        else:
            print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_game()
