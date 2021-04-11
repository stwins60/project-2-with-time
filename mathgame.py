import random

RAND_NUM = random.randrange(1, 100)

Guess = 5
Keep_playing = True
while Keep_playing:
    userGuess = int(input("Guess a number between 1 and 100: "))
    Guess -= 1
    if userGuess > 100:
        print("Guess number should not be greater than 100")
        break
    if userGuess < RAND_NUM:
        print("Number is too low!!!")
        
    elif userGuess > RAND_NUM:
        print("Number is too high!!!")
        
    elif userGuess == RAND_NUM:
        print("Your Guess the number " + str(RAND_NUM) + " Right")

    if Guess == 0:
        print("You ran out of guesses...")
        Keep_playing = False