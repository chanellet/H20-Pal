from pyfiglet import figlet_format
from colorama import init, Fore
from auth import login_user, register_user
from hydration import hydration_tracker
from emoji import emojize

init(autoreset = True) #reset for colorama .style
def main():
    print(Fore.LIGHTBLUE_EX + figlet_format('Welcome to H20 Pal!'))

    user = None
    while not user: #main menu for login/register/exit program
        print('\n[1] Login')
        print('[2] Register')
        print('[3] Exit')
        choice = input('\nChoose an option: ')
        
        #login
        if choice == '1':
            user = login_user()
            
        #register    
        elif choice == '2':
            user = register_user()
        
        #exit program    
        elif choice == '3':
            print(emojize(Fore.BLUE + '\nStay hydrated! :droplet:'))
            return
        else:
            print(Fore.RED + 'Invalid option. Try again!')
    if user:
        print(Fore.GREEN + f'Hello, {user}!') #welcomes user
     
    #per user file    
    tracker = hydration_tracker(username=user)
    tracker.load_from_file()

    while True:
        print(Fore.BLUE + '\nWhat would you like to do today?') #main options once logged in
        print('[1] Log water intake')
        print('[2] Set daily goal')
        print('[3] Today\'s total intake')
        print('[4] View history')
        print('[5] Logout')
        print('[6] Exit')
    
        choice = (input('Please enter a menu number: '))
    
        if choice == '1':
            try:
                amount = int(input('Enter amount in mls: '))
                tracker.add_entry(amount)
                print(Fore.GREEN + f'Successfully added {amount}mls!')
            except ValueError:
                print(Fore.RED + 'Unsuccessful! Please add a valid number.')
                
        elif choice == '2':
            try:
                new_goal = int(input('Enter new daily hydration goal in mls: '))
                tracker.set_goal(new_goal)
                tracker.save_to_file()
                print(Fore.CYAN + f'Goal set to {new_goal}mls')
            except ValueError:
                print(Fore.RED + 'Please enter a valid number!')
                
        elif choice == '3':
            total = tracker.total_today()
            print(f'\nTotal today: {total} mls')
            
        elif choice == '4':
            tracker.view_history()
            
        elif choice == '5':
            print(Fore.YELLOW + f'Successfully logged out...')
            print(Fore.LIGHTYELLOW_EX + 'Thank you for using H20 Pal!')
            return main()
        
        elif choice == '6':
            print(emojize(Fore.BLUE + '\nStay hydrated! :droplet:'))
            break
        else:
            print(Fore.RED + 'Invalid choice. Please select a valid option from the menu!')
        
if __name__ == '__main__':
    main()
        
            
            
        