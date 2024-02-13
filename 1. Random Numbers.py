import random

def guess_the_number():
    # Generate a random number between 0 to 10
    secret_number = random.randint(0,10)

    # Generate a counter
    counter = 0

    while True:
        Guess = int(input("Can you guess a number between 0 to 10? "))

        # Check if the number between 0 to 10 only
        if Guess > 10 or Guess < 0:
            print("Please enter a valid number between 0 to 10 only")
            continue

        counter += 1        

        if Guess > secret_number:
            print("Too High! Try again")
        elif Guess < secret_number:
            print("Too Low! Try again") 
        else:
            print(f"You are correct, the number was {secret_number}, You got that after {counter} times")               
            break
        
guess_the_number()        

