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
    choice = input("Would you like to generate a password or passphrase? (Enter 'password' or 'passphrase'): ").strip().lower()

    # Step 2: User chooses the length
    if choice == 'password':
        length = int(input("Enter the length of the password: "))
    elif choice == 'passphrase':
        length = int(input("Enter the number of words in the passphrase: "))
    else:
        print("Invalid choice. Please restart the program.")
        return

    # Step 3: User chooses the character sets for passwords
    if choice == 'password':
        char_sets = []
        if input("Include uppercase letters? (y/n): ").strip().lower() == 'y':
            char_sets.append(string.ascii_uppercase)
        if input("Include lowercase letters? (y/n): ").strip().lower() == 'y':
            char_sets.append(string.ascii_lowercase)
        if input("Include numbers? (y/n): ").strip().lower() == 'y':
            char_sets.append(string.digits)
        if input("Include symbols? (y/n): ").strip().lower() == 'y':
            char_sets.append(string.punctuation)

        if not char_sets:
            print("No character sets selected. Please restart the program.")
            return

    # Step 4: User chooses the number of passwords/phrases to generate
    num_generate = int(input("Enter the number of passwords/phrases to generate: "))


    # Step 5: User chooses spaces or special for passphrase
    spcChoice = input("Would you like to replace space between words with a special character? y/n ").strip().lower()

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
