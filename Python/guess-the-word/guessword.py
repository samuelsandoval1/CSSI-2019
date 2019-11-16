import random

Word = (' apple ' )
# # word = random.choice(Word)
#
# letter_guess = ''
# word_guess = ''
# store_letter = ''
# count = 0
# limit = 5

print ('Welcome to Guess the Word !!!!')
print ('You have 5 chances at guessing letters in a word')
print ('Let\s start!')
print ('\n')

wordlist = ['_'] * 5

while True:
    letter_guess = raw_input('Guess at letter:')
    print wordlist
    for letter in wordlist:
        print letter
        if letter == letter_guess:
            print letter
        else:
            print("_")

#     if letter_guess in word:
#         print('yes!')
#         store_letter += letter_guess
#         count += 1
#     if letter_guess not in word:
#         print('no')
#     if count == 2:
#         print('\n')
#         clue_request = input('Would you like a clue?')
#         if clue_request == 'y':
#             print('\n')
#             print('CLUE: The first and last letter of the word is: ', clue)
#         if clue_request == 'n':
#             print('You\'re very brave!')
#
# print('\n')
# print('Now its time to guess. You have guessed',len(store_letter),'letters correctly.')
# print('These letters are: ', store_letter)
#
# word_guess = input('Guess the whole word: ')
# while word_guess:
#     if word_guess.lower() == correct:
#         print('Congrats!')
#         break
#
#     elif word_guess.lower() != correct:
#         print('Unlucky! The answer was,', word)
        break

print('\n')
input('Press Enter to leave the program')
