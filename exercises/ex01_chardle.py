"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730392257"

word: str = input("Enter a 5-character word: ")

if len(word) < 5:
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")

if len(character) > 1:
    print("Error: Character must be a single character.")
    exit()
    
print("Searching for " + character + " in " + word)
count: int = 0

if (word[0]) == character:
    count = count + 1
    print(character + " found at index 0")

if (word[1]) == character:
    count = count + 1
    print(character + " found at index 1")

if (word[2]) == character:
    count = count + 1
    print(character + " found at index 2")

if (word[3]) == character:
    count = count + 1
    print(character + " found at index 3")

if (word[4]) == character:
    count = count + 1
    print(character + " found at index 4")

if count == 0:
    print("No instances of " + character + " found in " + word)
else:
    if count == 1:
        print("1 instance of " + character + " found in " + word)
    else:
        print(str(count) + " instances of " + character + " found in " + word)