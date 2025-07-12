import random

print('Welcome to the Rock, Paper, Scissors Game!')
print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.")

choice=['rock', 'paper', 'scissors']    

while True:
    user_choice = input('Enter your choice: ').lower()

    if user_choice=='quit':
        print('Thank you for playing!')
        break

    if user_choice not in choice:
        print('Invalid choice. Please enter rock, paper, or scissors.')
        continue

    computer_choice = random.choice(choice)

    print(f'Computer chose: {computer_choice}')

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print('You win!')
    else:
        print('You lose!') 