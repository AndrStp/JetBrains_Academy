# Write your code here
from random import choice

label = 'hangman'
greeting = 'The game will be available soon.'

words = ['python', 'java', 'kotlin', 'javascript']
word = list(choice(words))

# Create new list for display with the same length of chars as in a word
guessed_word = ['-' for x in word]

# Create a set of all guessed letters
guessed_letters = set()

# The number of tries
tries = 8

print(f"{' '.join(label.upper())}")

option = None

while True:
    option = input('Type "play" to play the game, "exit" to quit: ').lower()

    if option == 'exit':
        break
    elif option == 'play':
        print()

        while tries > 0:

            print(''.join(str(n) for n in guessed_word))

            char = input("Input a letter: ")

            if len(char) > 1:
                print('You should input a single letter')
                print()
                continue

            elif not char.isalpha() or not char.islower():
                print('Please enter a lowercase English letter')
                print()
                continue

            if char in word:
                counter = 0

                if char not in guessed_letters:

                    guessed_letters.add(char)

                    for letter in word:
                        if char == letter:
                            guessed_word[counter] = char
                        counter += 1

                    if guessed_word == word:
                        print(f'You guessed the word {"".join(word)}!', 'You survived!', sep='\n')
                        print()
                        break

                else:
                    print('You\'ve already guessed this letter')
                    print()

                print()

            else:

                if char not in word and char in guessed_letters:
                    print('You\'ve already guessed this letter')
                else:
                    tries -= 1

                guessed_letters.add(char)

                if tries > 0:
                    print('That letter doesn\'t appear in the word')
                    print()
                else:
                    print('That letter doesn\'t appear in the word')
                    print('You lost!')

    else:
        break
