from pyfiglet import figlet_format
from colorama import init, Fore
from auth import login_user, register_user
from hydration import hydration_tracker
from emoji import emojize
import time

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
        #invalid input
        else:
            print(Fore.RED + 'Invalid option. Try again!')
    if user:
        print(Fore.GREEN + f'Hello, {user}!') #welcomes user
     
    #per user file - will create file for new user or load if data is available    
    tracker = hydration_tracker(username=user)
    tracker.load_from_file()

    #main options once logged in
    while True:
        print(Fore.BLUE + '\nWhat would you like to do today?') 
        print('[1] Log water intake')
        print('[2] Set daily goal')
        print('[3] Today\'s total intake')
        print('[4] View history')
        print('[5] Delete an entry')
        print('[6] Logout')
        print('[7] Exit')
    
        choice = (input('Please enter a menu number: '))
    
        #users water intake entry
        if choice == '1':
            try:
                amount = int(input('Enter amount in mls: '))
                tracker.add_entry(amount)
                print(Fore.GREEN + f'Successfully added {amount}mls!')
            except ValueError:
                print(Fore.RED + 'Unsuccessful! Please add a valid number.')
            time.sleep(2)
         
        #change hydration goal for the day    
        elif choice == '2':
            try:
                new_goal = int(input('Enter new daily hydration goal in mls: '))
                tracker.set_goal(new_goal)
                tracker.save_to_file()
                print(Fore.CYAN + f'Goal set to {new_goal}mls')
            except ValueError:
                print(Fore.RED + 'Please enter a valid number!')
            time.sleep(2)
        
        #show total water consumed for the day        
        elif choice == '3':
            total = tracker.total_today()
            print(f'\nTotal today: {total} mls')
            time.sleep(2)
        
        #shows users history    
        elif choice == '4':
            tracker.view_history()
            time.sleep(2)
            
        #deletes an existing entry
        elif choice == '5':
            if not tracker.entries:
                print('No entries to delete!')
                time.sleep(2)
            else:
                while True:
                    print('Select an entry to delete: \n')
                    for x, e in enumerate(tracker.entries, start=1):
                        print(f'[{x}] {e.date} - {e.amount} mls')
                    
                    try:
                        option = int(input('\nEnter number to delete or 0 to exit: '))
                        if option == 0:
                            print('Action cancelled! Returning to menu...')
                            time.sleep(2)
                            break
                        elif tracker.delete_entry(option - 1):
                            print('Entry deleted.')
                            time.sleep(2)
                            break
                        else:
                            print('Invalid number please try again!')
                    except:
                        print('Please enter a valid number.')
                        time.sleep(2)
        
        #logout of current user account            
        elif choice == '6':
            print(Fore.YELLOW + f'Successfully logged out...')
            print(Fore.LIGHTYELLOW_EX + 'Thank you for using H20 Pal!')
            time.sleep(2)
            return main()
        
        #exits program
        elif choice == '7':
            print(emojize(Fore.BLUE + '\nStay hydrated! :droplet:'))
            break
        
        #handles invalid input
        else:
            print(Fore.RED + 'Invalid choice. Please select a valid option from the menu!')
            time.sleep(2)
 
#safety code in case of future imports
if __name__ == '__main__':
    main()
        
            
            
        