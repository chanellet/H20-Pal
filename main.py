from pyfiglet import figlet_format
from colorama import init, Fore, Style
from auth import login_user, register_user
from hydration import tracker
from emoji import emojize

init(autoreset = True) #reset for colorama .style
def main():
    tracker = tracker()
    tracker.load_from_file()

print(Fore.LIGHTBLUE_EX + figlet_format('Welcome to H20 Pal!'))

user = None
while not user: #main menu for login/register/exit program
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
    print(Fore.GREEN + f'Hello, {user}!') #welcomes user

while True:
    print(Fore.BLUE + '\nWhat would you like to do today?') #main options once logged in
    print('[1] Log water intake')
    print('[2] Set daily goal')
    print('[3] Today\'s total intake')
    print('[4] Save')
    print('[5] Load')
    print('[6] View history')
    print('[7] Logout')
    print('[6] Exit')
    
    choice = (input('Please enter a menu number: '))
    
    if choice == '1':
        try:
            amount = int(input("Enter amount in ml: "))
            tracker.add_entry(amount)
            print(Fore.GREEN + f'Successfully added {amount}mls!')
        except ValueError:
            print(Fore.RED + 'Unsuccessful! Please add a valid number.')
    elif choice == '2':
        try:
            new_goal = int(input('Enter new daily hydration goal in ml: '))
            tracker.set_goal(new_goal)
            print(Fore.CYAN + 'Goal set to {new_goal}ml')
        except ValueError:
            print(Fore.RED + 'Please enter a valid number!')
    elif choice == '3':
        total = tracker.total_today()
        print(f'\nTotal today: {total} mls')
    elif choice == '4':
        tracker.save_to_file
    elif choice == '5':
        tracker.load_from_file
    elif choice == '6':
        tracker.view_history()
    elif choice == '7':
        print(Fore.YELLOW + f'Successfully logging out {user}...')
        break
    elif choice == '8':
        print(emojize(Fore.BLUE + '\nStay hydrated! :droplet:'))
    else:
        print(Fore.RED + 'Invalid choice. Please select a valid option from the menu!')
        
if __name__ == '__main__':
    main()
        
            
            
        