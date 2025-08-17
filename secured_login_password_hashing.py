# ==========================================================
#🔐 Secure Login System with Password Hashing
# Author: ADCarthan88
#Description: Gui-based user registration and login authentication system
# using bcrypt for secure password hashing.
# This script allows users to register with a username and password.
# ==========================================================

import bcrypt
import json
import os
import tkinter as tk
from tkinter import messagebox
#-------- GUI Setup -------------------
root = tk.Tk()
root.title('Secure Login System')
root.geometry('300x200')

username_label = tk.Label(root, text='Username')
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text='Password')
password_label.pack()
password_entry = tk.Entry(root, show='*')
password_entry.pack()

USER_DB = 'user.json'

#===================Setup user database===================
# Create user database if it doesn't exist
if not os.path.exists(USER_DB):
    with open(USER_DB, 'w') as f:
        json.dump({}, f)
#------------------- Auth Logic -------------------
def hash_password(password):
            return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(password, hashed):
            return bcrypt.checkpw(password.encode('utf-8'), hashed)
             
def register(username, password):
            with open(USER_DB, 'r') as f:
                users = json.load(f)
            if username in users:
                print("Username already exists.")
                return False
            hashed = hash_password(password)
            users[username] = hashed.decode('utf-8')
            with open(USER_DB, 'w') as f:
                json.dump(users, f)
            print("User registered successfully.")
            return True

def login(username, password):
            with open(USER_DB, 'r') as f:
                users = json.load(f)
                if username not in users:
                    print('USER NOT FOUND.')
                    return False

                stored_hash = users[username].encode('utf-8')
                if verify_password(password, stored_hash):
                    print('Login successful.')
                    return True
                else:
                    print('Incorrect password')
                    return False

if __name__ == '__main__':
    print('Welcome to the secure login system.')
    while True:
        action = input('Do you want to (r)egister, (l)ogin, or (q)uit? ').lower()
        if action == 'r':
            username = input('Enter a username: ')
            password = input('Enter a password: ')
            register(username, password)
        elif action == 'l':
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            login(username, password)
        elif action == 'q':
            break
        else:
            print('Invalid option. Please try again.')
def handle_register():
    username = username_entry.get()
    password = password_entry.get()
    register(username, password)
    messagebox.showinfo('Success', 'User registered successfully.')

def handle_login():
    username = username_entry.get()
    password = password_entry.get()
    if login(username, password):
        messagebox.showinfo('Success', 'Login Successful.')
    else:
        messagebox.showerror('Login Failed', 'Incorrect username.')

register_button = tk.Button(root, text='Register', command=handle_register)
register_button.pack()

login_button = tk.Button(root, text='Login', command=handle_login)
login_button.pack()
from colorama import Fore, Style

print(Fore.GREEN + '✅ Login successful!' + Style.RESET_ALL)
print(Fore.RED + '❌ Invalid credentials!' + Style.RESET_ALL)

username = input('👤 Enter your username: ')
password = input('🔒 Enter your password: ')
print("""
  ____                      _             
 / ___|  ___  ___ _ __ ___ (_)_ __   __ _ 
 \___ \ / _ \/ __| '_ ` _ \| | '_ \ / _` |
  ___) |  __/ (__| | | | | | | | | | (_| |
 |____/ \___|\___|_| |_| |_|_|_| |_|\__, |
                                    |___/ 
""")

root.mainloop()