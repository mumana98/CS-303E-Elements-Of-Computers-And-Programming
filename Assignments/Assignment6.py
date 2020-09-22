#Matthew Umana msu245

def locker_puzzle():
    arr = [False] * 100
    counter = 1
    for i in range(0, len(arr) + 1):
        counter2 = i
        for j in range(0, len(arr), counter):
            arr[j - 1] = not arr[j - 1]
            if counter > 100:
                pass    
        counter += 1

    for x in range(0, len(arr)):
        if arr[x]:
            print(x + 1)

def play_hangman():
    print("Let’s play hangman!")
    secret_word = "banjo"
    secret_word_list = []
    guessing = []
    guessing_str = ""
    correct_letters = []
    guesses = 8
    for x in secret_word:
        secret_word_list += [x]
    for i in secret_word:
        guessing += ["-"]
    for j in guessing:
        guessing_str += j
    print(guessing_str)
    while len(correct_letters) < len(guessing) and guesses > 0:
        guessed_letter = input("Guess a letter: ")
        if guessed_letter.isalpha() and len(guessed_letter) < 2:
            guessed_letter = guessed_letter.lower()
            result = secret_word.find(guessed_letter)
            if guessed_letter in correct_letters:
                print("You've already guessed", guessed_letter)
                continue
            elif result != -1:
                replace = secret_word_list.index(guessed_letter)
                guessing[replace] = guessed_letter
                correct_letters += guessed_letter
            else:
                guesses -= 1
                pass
        else:
            print("That is not a letter. Enter a letter.")
            continue
        guessing_str = ""
        for j in guessing:
            guessing_str += j
        if len(correct_letters) == len(guessing):
            print("You win!")
            continue
        elif guesses <= 0:
            print("You have " + str(guesses) + " tries remaining.")
            print("You lose.")
            continue
        display_word(guessing_str, correct_letters)
        print("You have " + str(guesses) + " tries remaining.")
    
def display_word(secret_word, guessed_letters):
    print(secret_word)

def main():
    locker_puzzle()
    play_hangman()
    
main()

