secret = 9
guess = -3
tries = 0
last_guess = None

while guess != secret:
    guess = int(input("Guess the number: "))

    if guess != last_guess:
        tries = tries + 1

    if guess > secret:
        print("Too large")
    elif guess < secret:
        print("Too small")

    last_guess = guess

print("Correct!")
print("Number of tries:", tries)