'''
Wordle  

Text file of 5 letter words: https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt

by Natalie Ohanjanians
December 28, 2023
'''
import random as rndm

def title(gamename):

    dash = "=" * len(gamename)

    print(dash)
    print(gamename)
    print(dash)

def read_file(filename):

    raw_file = open(filename, "r")
    file = raw_file.read().splitlines()
    raw_file.close()

    return file

def hint_indexes(answer, guess):
    '''
    search for matching characters, provide hint 
    '''
    answer_chars = list(answer)
    guess_chars = list(guess)
    slight_correct = []  # letter is somewhere in the word
    exact_correct = {}  # exact index as letter in word 

    for i in range(len(answer_chars)):
        for j in range(len(guess_chars)):

            if answer_chars[i] == guess_chars[j]:
                if i == j:
                    exact_correct[guess_chars[j]] = i
                else:
                    slight_correct.append(guess_chars[j])

    return exact_correct, slight_correct

def hint(exact_correct, slight_correct, guess):
    '''
    prints guess with exact_correct letters 
    '''
    hint_letters = ", ".join(slight_correct)
    hint_word = list(guess)

    for letter in exact_correct:
        letter_caps = letter.upper()
        hint_word[exact_correct[letter]]  = letter_caps
    

    return "".join(hint_word), hint_letters

def main():

    title("Wordle")
    print("Guess the right word! Letters correctly placed are capitalized in your guess, and correct letters in the wrong spot are listed. You get five tries!")

    word_list = read_file("5letterwords.txt")
    answer = word_list[rndm.randint(0, len(word_list))]
    rounds = 0
    guess = ""

    while rounds < 5:
        if answer != guess:

            guess = input("Guess a word:\n").lower()

            if guess in word_list:
                    rounds += 1
                    exact_correct, slight_correct = hint_indexes(answer, guess)
                    hint_word, hint_letters = hint(exact_correct, slight_correct, guess)

                    print(f"Guess: {hint_word}\nCorrect but misplaced: {hint_letters}")
                    print(f"You have {5 - rounds} tries remaining!")

            else:
                print("Invalid word, try again")

        else:
            print(f"Well done! The word was: {answer}")
            return
            
    print(f"Sorry, gane over. The word was {answer}")

main()