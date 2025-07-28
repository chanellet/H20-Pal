import os
from colorama import init, Fore, Style

init(autoreset = True)
user_file = 'users.txt'

def load_users():
    users = {}
    
    if os.path.exists(user_file):
        with open (user_file, 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                users[username] = password
    return users

def save_user(username, password):
    with open(user_file, 'a') as file:
        file.write(f'{username}, {password}\n')
        
def register_user():
    users = load_users()
    username = input('Input a username: ')
    if username in users:
        print(Fore.RED + 'That username already exists! Please log in or try again.')
        return None
    password = input('Choose a password: ')
    save_user(username, password)
    print('Registered successfully!')
    return username

def login_user():
    users = load_users()
    username = input('Username: ')
    if username not in users:
        print('Username not found! Please register or login')
        return None
    password = input('Password: ')
    if username in users and users[username] == password:
        print('Logged in successfully!')
        return username
    else:
        print('Login failed. Please try again!')
        return None