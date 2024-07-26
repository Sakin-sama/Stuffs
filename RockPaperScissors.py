import random

system = []
user_string = []
user = 0

def outcome(system_input, user):
    if system_input == user:
        return 'Its a Tie!'
    elif system_input == 1 and user == 2:
        return 'You won!'
    elif system_input == 1 and user == 3:
        return 'You lost!'
    elif system_input == 2 and user == 1:
        return 'You lost!'
    elif system_input == 2 and user == 3:
        return 'You won!'
    elif system_input == 3 and user == 1:
        return 'You won!'
    elif system_input == 3 and user == 2:
        return 'You lost!'
    
while 1:
    randnum = random.randint(1,3)
    system_input = randnum
    if randnum == 1:
        system.append('Rock')
    elif randnum == 2:
        system.append('Paper')
    elif randnum == 3:
        system.append('Scissors')

    print('System has made selection')
    print('Your turn to make a selection')
    print('choose Rock, Paper, or Scissors')
    user_string.append(input())
    print(user_string, system)
    if user_string == ['Rock']:
        user = 1
    elif user_string == ['Scissors']:
        user = 3
    elif user_string == ['Paper']:
        user = 2
    else:
        print('Invalid choice. Restarting')
        user_string.clear()
        system.clear()
    if user != 0:
        print(f'system chose: {system}')
        print(f'user chose: {user_string}')
        print(outcome(system_input, user))
        print('Play again? Y/N')
        user_string.clear()
        system.clear()
        if input() != 'Y':
            break
