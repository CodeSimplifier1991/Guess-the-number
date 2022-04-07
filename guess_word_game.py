# The number to be guessed
lucky_number = 29

# Initial message
message = " "

# The limited time a player can guess the number
guess_limit = 3

# Start with attempt
guess_count = 0

# The initial value for guessing is 0
entered_guessNumber = 0

# While the guessed number is less than the limited guess
while guess_count < guess_limit:

    # The player can enter their guess number
    entered_guessNumber = int(input("What is your guess? "))

    # On each round, the guess count will be added by 1
    guess_count += 1

    # If the number entered by the player matches the lucky number
    if entered_guessNumber == lucky_number:

        # The message will be shown
        message = "Hooray! You guessed it right!"

        # And the program will be terminated
        break

# If the player ran out of guess, the message below will be shown
else:
    message = "Sorry! You ran out of attempts!"

# The final message will be printed on the console
print(message)

