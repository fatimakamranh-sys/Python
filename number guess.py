import random

secret = random.randint(1, 100)
guess = 0
tries = 0

while guess != secret:
    guess = int(input("Guess a number between 1 and 100: "))
    tries = tries + 1
    
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print( f"You got it! 🎉  it took you {tries} tries")