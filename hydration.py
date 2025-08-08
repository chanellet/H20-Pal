from colorama import init, Fore, Style
from datetime import datetime
from tabulate import tabulate
import os

init(autoreset=True)

class hydration_entry: 
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount

#main logic for tracking user inputs and information        
class hydration_tracker: 
    def __init__(self, goal_ml=2000, username: str | None = None):
        self.entries: list[hydration_entry] = []
        self.goal_ml = goal_ml
        self.username = username
        self.filename = f'hydration_{username}.txt' if username else 'hydration_log.txt'
    
    #making sure the log file exists and starts with GOAL
    #internal use - non-public so we use '_' for python naming convention    
    def _ensure_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                f.write(f'GOAL,{self.goal_ml}\n')
    
    #auto adds to users entries, saves as a new line             
    def _append_entry_to_file(self, entry: hydration_entry): 
        self._ensure_file()
        with open(self.filename, 'a') as f:
            f.write(f'{entry.date},{entry.amount}\n')
    
    #write all to file including goal and all entries from username        
    def _write_to_file(self):
        with open(self.filename, 'w') as f:
            f.write(f'GOAL,{self.goal_ml}\n')
            for e in self.entries:
                f.write(f'{e.date},{e.amount}\n')
    
    #write/update users goal for the day    
    def set_goal(self, new_goal): 
        self.goal_ml = new_goal
        self._ensure_file()
        existing_entries = list(self.entries)
        self.load_from_file(self.filename)
        self.entries = existing_entries
        self._write_to_file()
     
    #user entries for the day    
    def add_entry(self, amount):
        today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        entry = hydration_entry(today, amount)
        self.entries.append(entry)
        self._append_entry_to_file(entry)
    
    #delete user entries  
    def delete_entry(self, listing):
        if listing < 0 or listing >= len(self.entries):
            return False
        self.entries.pop(listing)
        self._ensure_file()
        self._write_to_file()
        return True
    
    #total amount user has had for the day    
    def total_today(self):
        today = datetime.now().strftime('%Y-%m-%d')
        return sum(e.amount for e in self.entries if e.date.startswith(today))
    
    #user specific save to their username file
    def save_to_file(self, filename=None):
        if filename:
            self.filename = filename
        self._ensure_file()
        self._write_to_file()
    
    #user specific load from their file - if file not found one will be created when they log their first entry            
    def load_from_file(self, filename=None):
        if filename:
            self.filename = filename
        try:
            with open(self.filename, 'r') as f:
                self.entries = []
                for line in f:
                    if line.startswith('GOAL'):
                        _, goal = line.strip().split(',')
                        self.goal_ml = int(goal)
                    else:
                        date, amount = line.strip().split(',')
                        self.entries.append(hydration_entry(date, int(amount)))
        except FileNotFoundError: #for file not found
            print(Fore.RED + 'No history found!')
            print(Fore.LIGHTMAGENTA_EX + 'Let\'s get you started on your hydration journey!')
    
    #allows user to view their history        
    def view_history(self):
        table = [[e.date, f'{e.amount} ml'] for e in self.entries]
        print(tabulate(table, headers = ['Date & Time', 'Amount'], tablefmt='fancy_grid'))

