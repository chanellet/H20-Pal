from colorama import init, Fore, Style
from datetime import datetime
from tabulate import tabulate

init(autoreset=True)

class entry: 
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount
        
class tracker: 
    def __init__(self, goal_ml=2000):
        self.entries = []
        self.goal_ml = goal_ml
        
    def set_goat(self, new_goal): 
        self.goal_ml = new_goal
        
    def add_entry(self, amount):
        today = datetime.now().strftime("%Y-%m-%d")
        self.entries.append(entry(today, amount))
        
    def total_today(self):
        today = datetime.now().strftime("%Y-%m-%d")
        return sum(e.amount for e in self.entries if e.date == today)
    
    def save_to_file(self, filename="hydration_log.txt"):
        with open(filename, 'w') as f:
            f.write(f'GOAL,{self.goal_ml}\n')
            for e in self.entries:
                f.write(f'{e.date},{e.amount}\n')
                
    def load_from_file(self, filename="hydration_log.txt"):
        try:
            with open(filename, 'r') as f:
                self.entries = []
                for line in f:
                    if line.startswith("GOAL"):
                        _, goal = line.strip().split(',')
                        self.goal_ml = int(goal)
                    else:
                        date, amount = line.strip().split(',')
                        self.entries.append(entry(date, int(amount)))
        except FileNotFoundError: #for file not found
            print(Fore.RED + 'No history found!')
            
    def view_history(self):
        table = [[e.date, f'{e.amount} ml'] for e in self.entries]
        print(tabulate(table, headers = ['Date', 'Amount'], tablefmt='fancy_grid'))

