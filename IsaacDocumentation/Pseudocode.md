# Secure Password Generator Pseudocode:

### Requirements:

1. Allow users to choose whether they would like to generate a password or passphrase.

2. Allow users to choose the length of the password/phrase. (The number of characters for a password /or the number of words for a passphrase.)

3. Allow the user to choose the character sets they wish to use, eg. uppercase, lowercase, numbers, symbols.

4. Allow the user to choose the number of passwords/phases they would like to generate.

5. Allow the user to choose an output file to place the generated password(s). (enabled with command line option i.e. -o)

6. The results should always be printed to the screen and optionally an output file.

### Pseudocode:
```
IMPORT required modules

OPEN word dictionaries
  SET [Words] as dictionaries content

SET [specialChars] as '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
SET [special] as random digit in [specialChars]

DEFINE generate password function
  SET [characterPool] as inputed choice of [character sets]
  RETURN password using the character pool and inputed length

DEFINE generate passphrase
  RETURN passphrase using [Words] and using [special] as space between words and inputed length

DEFINE main function
  DEFINE arg parser for "-o" and "--ouput" used for saving password to output file

  INPUT password or passphrase

  IF password
    SET [character sets] as list
    INPUT include uppercase? y/n
    IF y
      ADD to [character sets]
    INPUT include lowercase? y/n
    IF y
      ADD to [character sets]
    INPUT include numbers? y/n
    IF y
      ADD to [character sets]
    INPUT include symbols? y/n
    IF y
      ADD to [character sets]

  INPUT number of passwords/phrases to generate as [num generate]

  SET 

```
