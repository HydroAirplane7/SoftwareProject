# Secure Password Generator Pseudocode:

### Requirements:

1. Allow users to choose whether they would like to generate a password or passphrase.

2. Allow users to choose the length of the password/phrase. (The number of characters for a password /or the number of words for a passphrase.)

3. Allow the user to choose the character sets they wish to use, eg. uppercase, lowercase, numbers, symbols.

4. Allow the user to choose the number of passwords/phases they would like to generate.

5. Allow the user to choose an output file to place the generated password(s). (enabled with command line option i.e. -o)

6. The results should always be printed to the screen and optionally an output file.

### Pseudocode:

IMPORT required modules

SET variable WordOrPhrase
SET variable Length
SET variable Lower
SET variable Upper
SET variable Numbers
SET variable Symbols
SET variable DoExport
SET variable OutFile

OUTPUT "Welcome to the Secure Password Generator Program!"

OUTPUT "Would you like to make a Password or Passphrase? "
INPUT (password/passphrase response) = WordOrPhrase
IF WordOrPhrase == password
    OUTPUT "How many characters long should the Password be? "
    INPUT (integer) = Length
ELSE 
    OUTPUT "How many words long should the Password be? "
    INPUT (integer) = Length

OUTPUT "For the following, type YES or NO for the character sets you want included in the Password/phrase"
OUTPUT "Lowercase letters: "
INPUT (YES/NO) = Lower
DO INPUT check and display error if answer is not YES or NO
OUTPUT "Uppercase letters: "
INPUT (YES/NO) = Upper
DO INPUT check and display error if answer is not YES or NO
OUTPUT "Numbers: "
INPUT (YES/NO) = Numbers
DO INPUT check and display error if answer is not YES or NO
OUTPUT "Symbols: "
INPUT (YES/NO) = Symbols
DO INPUT check and display error if answer is not YES or NO

OUTPUT "Would you like to save the Passwords/Passphrases to a file? "
INPUT (YES/NO) = DoExport
DO INPUT check and display error if answer is not YES or NO
IF DoExport == YES 
    OUTPUT "What would you like the file to be called?"
    INPUT (string) = OutFile
