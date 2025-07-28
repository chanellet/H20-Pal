from pyfiglet import figlet_format
from colorama import init, Fore, Style
from auth import login_user, register_user
from emoji import emojize

init(autoreset = True)

print(Fore.LIGHTBLUE_EX + figlet_format('Welcome to H20 Pal!'))

user = None
while not user:
    print('\n[1] Login')
    print('[2] Register')
    print('[3] Exit')
    choice = input('\nChoose an option: ')
    if choice == '1':
        user = login_user()
    elif choice == '2':
        user = register_user()
    elif choice == '3':
        print(emojize(Fore.BLUE + '\nStay hydrated! :droplet:'))
        break
    else:
        print(Fore.RED + 'Invalid option. Try again!')
if user:
    print(Fore.GREEN + f'Hello, {user}!')

'''while True:
    print(Fore.BLUE + '\nWhat would you like to do today?')
    print('[1] Log water intake')
    print('[2] Set daily goal')
    print('[3] Today\'s total intake')
    print('[4] View history')
    print('[5] Logout')
    print('[6] Exit')
    
    try:
        choice = int(input('Please enter a menu number: '))'''
        