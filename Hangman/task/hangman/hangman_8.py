from random import choice


def main():
    words = ['python', 'java', 'kotlin', 'javascript']
    word = choice(words)
    print('H A N G M A N')
    while True:
        game = menu()
        if game == 'play':
            play(8, word)
        else:
            break


def play(guesses: int, word_to_guess: str):
    letters = set(word_to_guess)
    guessed_letters = set()
    word_display = ['-' for letter in word_to_guess]
    print()
    while guesses:
        print(''.join(word_display))
        guess = take_letter()
        if not guess:
            continue

        if guess in guessed_letters:
            print('You\'ve already guessed this letter')
        elif guess not in letters:
            guesses -= 1
            guessed_letters.update(guess)
            print('That letter doesn\'t appear in the word')
        else:
            guessed_letters.update(guess)
            for i in range(len(word_display)):
                if guess == word_to_guess[i]:
                    word_display[i] = guess

        end = is_end(word_display, guesses)
        if not end:
            print()
        elif end == 'win':
            print(f'You guessed the word {word_to_guess}!')
            print('You survived!')
            break
        else:
            print('You lost!')
            break

def take_letter():
    guess = input('Input a letter: ')
    if len(guess) > 1:
        print('You should input a single letter\n')
    elif not guess.isalpha() or not guess.islower():
        print('Please enter a lowercase English letter\n')
    else:
        return guess


def is_end(wordie: str, num_guesses: int):
    if wordie.count('-') < 1:
        return 'win'
    elif num_guesses == 0:
        return 'lose'


def menu() -> str:
    choices = ['play', 'exit']
    while True:
        game = input('Type "play" to play the game, "exit" to quit: ')
        if game in choices:
            return game


if __name__ == '__main__':
    main()
