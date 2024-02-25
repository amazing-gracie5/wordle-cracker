import random

with open('og_word_list', 'r') as in_file:
    data = in_file.read()
    og_word_string = data.lower()

word_list = og_word_string.split(" ")

def check_index(attempt, compare):
    for i in range(0,5):
        if (attempt[i] != '*'):
            if (attempt[i] != compare[i]):
                return False
    return True

def check_exclude(excluded, compare):
    for char in excluded:
        if char in compare:
            return False
    return True

def check_include(included, compare):
    for char in included:
        if char not in compare:
            return False
    return True

# this function will take your input and reccomend 5-letter words that fit your guesses so far
def crack_wordle():
    know = input("Enter what you know, use * for what you don't: ")
    unknown_index = input("Enter unknown index letters (no spaces): ")
    exclude = input("Enter letters that are not in the word: ")
    for i in range(0, len(word_list)):
        if (check_index(know, word_list[i]) and check_exclude(exclude, word_list[i]) and check_include(unknown_index, word_list[i])):
            print(word_list[i])
            
crack_wordle()

# this function will generate a wordle puzzle and let you play
def play_wordle():
    wordle = word_list[random.randint(0, len(word_list) - 1)]

    for x in range(6,0, -1):
        print("You have", x, "guesses left")
        guess = input("Enter your guess: ")
    
        if (guess == wordle):
            print("Yay, you won! The word is:")
            break
        else:
            #check word
            for i in range(0,5):
                #check letter
                print(guess[i] + ": ", end='')
                if guess[i] in wordle:
                    if (guess[i] == wordle[i]):
                        print("Correct index")
                    else:
                        print("Correct letter, wrong index")
                else:
                    print("Letter not in wordle")
    print(wordle)

play_wordle()