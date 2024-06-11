# Name: Joshua Kovzan, Raja MC
# Contact: Bootlessfire@gmail.com
# Date created: 27/05/2024
# Last updated: 11/06/2024


import secrets
import string
import argparse

# Setting up Mark's wordlist for passphrase words
with open('adjectives.txt', 'r') as f:
    adjectives = [line.strip() for line in f]

with open('nouns.txt', 'r') as f:
    nouns = [line.strip() for line in f]

with open('verbs.txt', 'r') as f:
    verbs = [line.strip() for line in f]

# Special characters for spacing in passphrase
specialChars = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'


def generate_password(length, char_sets):
    char_pool = ''.join(char_sets)
    return ''.join(secrets.choice(char_pool) for _ in range(length))


def generate_passphrase(length):
    return ' '.join(secrets.choice(adjectives + nouns + verbs) for _ in range(length))


def generate_passphrase_special(length):
    return f'{secrets.choice(specialChars)}'.join(secrets.choice(adjectives + nouns + verbs) for _ in range(length))
    #  ^ choice in the f-string for different character each passphrase


def main():
    # Setting up argument parser
    parser = argparse.ArgumentParser(description="Generate secure passwords or passphrases.")
    parser.add_argument('-o', '--output', type=str, help="Output file to save the generated passwords/phrases.")
    args = parser.parse_args()

    # Step 1: User chooses between password and passphrase
    while True:
        choice = input(
            "Would you like to generate a password or passphrase? (Enter 'password' or 'passphrase'): \n").strip().lower()
        if choice in ["password", "passphrase"]:
            break
        else:
            print("please enter 'password' or 'passphrase' to continue.")
        # added while loop to loop if incorrect entry

    # Step 2: User chooses the length
    while True:
        if choice == 'password':
            try:
                length = int(input("Enter the length of the password: \n"))
                if length > 0:
                    break
                else:
                    print("Please enter a positive integer")
            except ValueError:
                print("Please enter a positive integer.")

        elif choice == 'passphrase':
            try:
                length = int(input("Enter the number of words in the passphrase: \n"))
                if length > 0:
                    spcChoice = input(
                        "Would you like to replace space between words with a special character? y/n \n").strip().lower()
                    break
                    #  had to add spcChoice here to avoid it being prompted in password path
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Please enter a positive integer.")
            # added try/excpet to avoid value errors if user doesn't add integers

    # Step 3: User chooses the character sets for passwords
    if choice == 'password':
        char_sets = []
        while True:
            upper = input("Include uppercase letters? (y/n): \n").strip().lower()
            if upper == "y":
                char_sets.append(string.ascii_uppercase)
                break
            elif upper == "n":
                break
            else:
                print("Please enter 'y' or 'n'")

        while True:
            lower = input("Include lowercase letters? (y/n): \n").strip().lower()
            if  lower == "y":
                char_sets.append(string.ascii_lowercase)
                break
            elif lower == "n":
                break
            else:
                print("Please enter 'y' or 'n'")
        while True:
            numbers = input("Include numbers? (y/n): \n").strip().lower()
            if numbers == "y":
                char_sets.append(string.digits)
                break
            elif numbers == "n":
                break
            else:
                print("Please enter 'y' or 'n'")
        while True:
            symbols = input("Include symbols? (y/n): \n").strip().lower()
            if symbols == 'y':
                char_sets.append(string.punctuation)
                break
            elif symbols == "n":
                break
            else:
                print("Please enter 'y' or 'n'")

        if not char_sets:
            print("No character sets selected. Please restart the program.")
            return

    # Step 4: User chooses the number of passwords/phrases to generate
    while True:
        try:
            num_generate = int(input("Enter the number of passwords/phrases to generate: \n"))
            if num_generate > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a positive integer.")
        #  ^ added try/except to make sure num_generate was an integer

    # Generate and display the passwords or passphrases
    results = []
    for _ in range(num_generate):
        if choice == 'password':
            result = generate_password(length, char_sets)
        elif choice == 'passphrase':
            if spcChoice == 'y':
                result = generate_passphrase_special(length)
            elif spcChoice == 'n':
                result = generate_passphrase(length)
        results.append(result)
        print(result)

    # Step 5: Optionally save to an output file
    if args.output:
        with open(args.output, 'w') as file:
            for result in results:
                file.write(result + '\n')


if __name__ == "__main__":
    main()

'''
Run the script without specifying an output file
python generate_passwords.py


Run the script with an output file
python generate_passwords.py -o output.txt

'''
