#RANDOM PASSWORD MANAGER

import random
import string

def get_length():
    while True:
        value = input("Enter desired password length (minimum 8): ")
        try:
            length = int(value)
            if length < 8:
                print("Error: Length must be at least 8.")
                continue
            return length
        except ValueError:
            print("Error: Please enter a valid whole number.")

def get_character_types():
    print("\nChoose character types to include (yes/no):")
    types = {}
    types['upper'] = input("Include uppercase letters? (y/n): ").lower() == 'y'
    types['lower'] = input("Include lowercase letters? (y/n): ").lower() == 'y'
    types['digits'] = input("Include numbers? (y/n): ").lower() == 'y'
    types['symbols'] = input("Include symbols? (y/n): ").lower() == 'y'

    selected_count = sum(types.values())
    if selected_count < 2:
        print("Error: Please select at least 2 character types.\n")
        return get_character_types()

    return types

def build_character_pool(types):
    pool = ""
    if types['upper']:
        pool += string.ascii_uppercase
    if types['lower']:
        pool += string.ascii_lowercase
    if types['digits']:
        pool += string.digits
    if types['symbols']:
        pool += string.punctuation
    return pool

def generate_password(length, pool):
    return ''.join(random.choice(pool) for _ in range(length))

while True:
    length = get_length()
    types = get_character_types()
    pool = build_character_pool(types)

    password = generate_password(length, pool)
    print(f"\nGenerated Password: {password}")

    again = input("\nGenerate another password? (y/n): ").lower()
    if again != 'y':
        print("Goodbye!")
        break
    print()
