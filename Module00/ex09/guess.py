import random

magic_number = random.randint(1, 99)
guess = 0

print("Guess a number between 1 and 99 (included):")

while guess != magic_number:
	guess = input("> ")
	try:
		guess = int(guess)
	except:
		print("Not a number!")
		continue
	if guess == magic_number:
		if magic_number == 42:
			print("Looks like you guessed the answer of life, "
					"the universe and everything...\n"
					"And you were right, the answer is 42.")
		else:
			print("You guessed right!")
	elif guess > magic_number:
		print("Too high!")
	else:
		print("Too low!")