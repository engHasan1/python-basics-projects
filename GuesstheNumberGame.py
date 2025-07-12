import random
import time

print('welcome to the Guess the Number Game!')

randomNumber=random.randint(1, 100)
print('I have selected a random number between 1 and 100.')
print('Try to guess it! You have 10 attempts.')

startTime=time.time()
for i in range(10):
    print(f'Attempt {i + 1}:')
    try:
        guess=int(input('Enter your guess: '))
    except ValueError:
        print('Invalid input. Please enter a valid number between 1 and 100.')
        continue
    if guess<randomNumber:
        print('Too low! Try again.')
        pass
    elif guess>randomNumber:
        print('Too high! Try again.')
        pass
    else:
        print(f'Congratulations! You guessed the number {randomNumber} correctly in {i + 1} attempts!')
        break


endTime = time.time()   
elapsedTime = round(endTime - startTime, 2)
print(f"You finished the game in {elapsedTime} seconds.")
