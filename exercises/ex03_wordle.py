"""Structured Wordle."""

__author__ = "730392257"


# first function definition, finds if char is in guess
def contains_char(word: str, character: str) -> bool:
    """Searches for character in string."""
    assert len(character) == 1  # assures that the character = 1
    index: int = 0
    while index < len(word): 
        if word[index] == character:
            return True
        index += 1
    return False  # if character is not found in the word, must return false


# variables for emojies for next section (emojified)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Emoji ascribed to each character of guess string."""  # depends on whether character exists and in what spot
    assert len(guess) == len(secret)
    emoji: str = ""
    emoji_index: int = 0
    while emoji_index < len(guess):
        if guess[emoji_index] == secret[emoji_index]:
            emoji += GREEN_BOX
        elif contains_char(secret, guess[emoji_index]) is True:  # calls contains_char function to determine whether character exists
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX  # character does not exist in the secret word
        emoji_index += 1
    return emoji  # returns final string of emojis


def input_guess(expected_length: int) -> str:
    """Prompt user for guess and check for expected length."""
    wordle_guess: str = input(f"Enter a {expected_length} character word: ")
    while len(wordle_guess) != expected_length:
        wordle_guess = input(f"That wasn't {expected_length} chars! Try again: ")  # needs to be correct length
    return wordle_guess  # returns the guess when it is the correct length


def main() -> None:
    """The entrypoint of the program and main game loop."""
    answer: str = "codes"  # the word the user is trying to guess
    turns: int = 1  # starts at 1 because there is no 0/6 turns
    win: bool = False
    answer_length: int = len(answer)  # used for calling input_guess
    while turns <= 6 and win is False:  # if one of these is not correct then loop ends
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(answer_length)  # uses variable to make sure guess is correct length
        print(emojified(guess, answer))  # prints emoji line of the guess corresponding to answer
        if guess == answer:
            win = True  # ends loop
        else:
            turns += 1
    if win is True:
        return print(f"You won in {turns}/6 turns!")
    else:
        return print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()