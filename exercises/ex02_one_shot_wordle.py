"""EX02 - One Shot Wordle."""

__author__ = "730392257"

wordle: str = "python"
length: int = len(wordle)  # length of secret word
guess: str = input(f"What is your {length}-letter guess? ")

# variables for emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index: int = 0
emoji: str = ""
# Makes sure the right number of letters are in the guessed word
while len(guess) != length:
    guess = input(f"That was not {length} letters! Try again: ")

# checks each index to see if letter in guess matches letter in wordle
while index < length:
    if guess[index] == wordle[index]:
        emoji += GREEN_BOX
    else:
        character_exists: bool = False
        alternate: int = 0  # alternate indices of wordle
        # tests if letter in guessed word is in any spot in wordle (yellow square)
        while character_exists is not True and alternate < length:
            if wordle[alternate] == guess[index]:
                character_exists = True
            else:
                alternate += 1
        if character_exists is True:
            emoji += YELLOW_BOX    
        else:
            emoji += WHITE_BOX
    index += 1
   
print(emoji)  # prints the green, yellow, and white boxes corresponding to letters in wordle.

if guess == wordle:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")