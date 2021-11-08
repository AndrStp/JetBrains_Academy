import requests
from bs4 import BeautifulSoup


def main():
    languages = {
        1: 'Arabic', 2: 'German',
        3: 'English', 4: 'Spanish',
        5: 'French', 6: 'Hebrew',
        7: 'Japanese', 8: 'Dutch',
        9: 'Polish', 10: 'Portuguese',
        11: 'Romanian', 12: 'Russian',
        13: 'Turkish'
    }

    source_language, target_language, word_to_translate = take_args(languages)

    if not target_language:
        translate_all(source_language, word_to_translate, languages)

    else:
        response = get_response(source_language, target_language, word_to_translate)
        words, source_sentences, target_sentences = pull_data(response)
        save_results(word_to_translate, target_language, words, source_sentences, target_sentences)
        output_translations(target_language, words, source_sentences, target_sentences)


def take_args(languages: dict[int: str]) -> tuple[str, str, str]:
    """
    Return args from the user
    :return tuple of both source and target language and word
    """
    print('Hello, you\'re welcome to the translator. Translator supports:')
    for i, value in languages.items():
        print(f'{i}. {value}')

    source_language = languages.get(int(input('Type the number of your language:\n'))).lower()

    print("Type the number of language you want to translate or "
          + "'0' to translate to all languages:")
    target_language = languages.get(int(input()))
    if target_language:
        target_language = target_language.lower()

    word_to_translate = input('Type the word you want to translate:\n')
    print()

    return source_language, target_language, word_to_translate


def get_response(src_lang: str, trg_lang: str, word: str) -> requests.Response:
    """
    Return the Response object
    :param src_lang : source language
    :param trg_lang : target language
    :param word : words to translate
    :returns : Response
    """
    url = f'https://context.reverso.net/translation/{src_lang}-{trg_lang}/{word}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    return response


def check_response(response: requests.Response) -> tuple[int, str]:
    """
    Return status code and status of the given response
    :param response: requests.Response
    :returns : tuple of status code and status
    """
    if response.ok:
        return response.status_code, 'OK'
    return response.status_code, 'Failed'


def pull_data(response: requests.Response) -> tuple[list[str], list[str], list[str]]:
    """
    Pulls the words and sentences from the given Response
    :param response: requests.Response
    :returns : tuple of three lists: [words], [source_sentences], [target_sentences]
    """
    soup = BeautifulSoup(response.text, 'html.parser')
    words = [word.text.strip() for word in soup.find(id='translations-content').find_all('a')]

    source_sentences = [sentence.text.strip()
                        for sentence
                        in soup.find(id='examples-content').find_all('div', class_='src ltr')]
    target_sentences = [sentence.text.strip()
                        for sentence
                        in soup.find(id='examples-content').find_all('div',
                                                                     class_=['trg ltr',
                                                                             'trg rtl arabic',
                                                                             'trg rtl'])]
    return words, source_sentences, target_sentences


def output_translations(
        language: str,
        words: list[str],
        source_sentences: list[str],
        target_sentences: list[str]) -> None:
    """
    Outputs the translations to the console in the fancy way
    :param language : target language
    :param words : list of translations to the word
    :param source_sentences : list of source language sentences
    :param target_sentences : list of target language sentences (translations)
    """
    print(f'{language.capitalize()} Translations:')
    print(words[0] + '\n')
    print(f'{language.capitalize()} Examples:')
    print(source_sentences[0] + ':\n' + target_sentences[0] + '\n')


def translate_all(src_lang: str, word: str, all_lang: dict) -> None:
    """
    Writes translations to file word-name.txt for all supported languages
    :param src_lang: source language
    :param word word: to translate
    :param all_lang: dict of all available languages
    """
    with open(f'{word}.txt', 'a+', encoding='utf-8') as f:
        for lang in all_lang.values():
            if lang.lower() == src_lang:
                continue

            response = get_response(src_lang, lang.lower(), word)
            words, source_sentences, target_sentences = pull_data(response)
            save_results(word, lang, words, source_sentences, target_sentences)
            output_translations(lang, words, source_sentences, target_sentences)


def save_results(word: str,
                 lang: str,
                 words: list[str],
                 src_sentences: list[str],
                 trg_sentences: list[str]) -> None:
    """
    :param word: word to translate
    :param lang: target language
    :param words: list of translations to the word
    :param src_sentences: list of source language sentences
    :param trg_sentences: list of target language sentences (translations)
    :return: None
    """
    with open(f'{word}.txt', 'a+', encoding='utf-8') as f:
        f.write(f'{lang.capitalize()} Translations:\n')
        f.write(words[0] + '\n\n')
        f.write(f'{lang.capitalize()} Examples:\n')
        f.write(src_sentences[0] + ':\n' + trg_sentences[0] + '\n\n')


if __name__ == '__main__':
    main()
    # status_code, status = check_response(response)
    # print(f'You chose "{target_language}" as a language to translate "{word_to_translate}".')
    # print(status_code, status)
