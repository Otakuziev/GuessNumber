import random
from replit import clear
from Logo import logo
def guessNumber():
	print("Wellcome to the Number Guessing Game!")
	computerNumber = random.randint(1, 100)
	print(logo)

	print("I am thinking a number between 1 and 100.")
	level = input("Choose a difficulty: Type 'easy' or 'hard': ")

	if level == "easy":
		attempts = 10
		print(f"You have {attempts} attempts remaining to guess the number!")
	else:
		attempts = 5
		print(f"You have {attempts} attempts remaining to guess the number!")
	userNumber = 0.0
	while userNumber != computerNumber:
		userNumber = int(input("Make a guess: "))
		if userNumber == computerNumber:
			print(f"You got it! The answer was {computerNumber}")
			newGame = input("Do you want to play again? Type 'y' to start new game, or type 'n' to finish: ")
			if newGame == 'y':
				clear()
				guessNumber()
		elif userNumber < computerNumber:
			print("Too low!")
			attempts -= 1
			print(f"You have {attempts} remaining!")
		elif userNumber > computerNumber:
			print("Too high!")
			attempts -= 1
			print(f"You have {attempts} remaining!")
			if attempts == 0:
				print("You lose :)!")
			else:
				print("Guess one more time!")
guessNumber()