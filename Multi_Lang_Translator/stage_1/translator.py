def main():
    print('Type "en" if you want to translate from French into English, \
    or "fr" if you want to translate from English into French:')
    language = input()

    print('Type the word you want to translate:')
    word_to_translate = input()

    print(f'You chose "{language}" as the language to translate "{word_to_translate}" to.')


if __name__ == '__main__':
    main()
