import random

default_options = ['rock', 'paper', 'scissors']

# Welcome message
user_name = input('Enter your name: ')
print('Hello, ' + user_name)

# Get game options
game_options = input()
if len(game_options) == 0:
    game_options = default_options
else:
    game_options = game_options.split(',')

print("Okay, let's start")

# set valid inputs
valid_input = game_options + ['!exit', '!rating']

# Get rating
user_rating = 0
ratings_file = open('rating.txt', 'r')
for line in ratings_file:
    if user_name in line:
        user_rating = int(line.replace('\n', '').split()[1])
        break
ratings_file.close()

# Game loop
while True:
    user_choice = input()
    
    # check if game ends
    if user_choice == '!exit':
        print('Bye!')
        break
        
    # check rating
    if user_choice == '!rating':
        print('Your rating: ', user_rating)
        continue
    
    # handle invalid input
    if user_choice not in valid_input:
        print('Invalid input')
        continue
    
    # find the winning and losing options
    choice_idx = game_options.index(user_choice)
    other_choices = game_options[choice_idx + 1:] + game_options[:choice_idx]
    winning_options = other_choices[:len(game_options) // 2]
    losing_options = other_choices[len(game_options) // 2:]
    
    # make a choice for the computer
    computer_choice = random.choice(game_options)

    if user_choice == computer_choice:
        print(f"There is a draw ({user_choice})")
        user_rating += 50
    elif computer_choice in losing_options:
        print(f"Well done. Computer chose {computer_choice} and failed")
        user_rating += 100
    elif computer_choice in winning_options:
        print(f"Sorry, but computer chose {computer_choice}")
