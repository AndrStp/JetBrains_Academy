import requests
from bs4 import BeautifulSoup


def main():
    source_language, target_language, word_to_translate = take_args()
    response = get_response(source_language, target_language, word_to_translate)

    words, source_sentences, target_sentences = pull_data(response)
    output_translations(target_language, words, source_sentences, target_sentences)


def take_args() -> tuple[str, str, str]:
    """
    Return args from the user
    :return tuple of both source and target language and word
    """
    languages = {
        1: 'Arabic',
        2: 'German',
        3: 'English',
        4: 'Spanish',
        5: 'French',
        6: 'Hebrew',
        7: 'Japanese',
        8: 'Dutch',
        9: 'Polish',
        10: 'Portuguese',
        11: 'Romanian',
        12: 'Russian',
        13: 'Turkish'
    }
    print('Hello, you\'re welcome to the translator. Translator supports:')
    for i, value in languages.items():
        print(f'{i}. {value}')
    language_from = languages.get(int(input('Type the number of your language:\n'))).lower()
    language_to = languages.get(int(input('Type the number of language you want to translate on:\n'))).lower()
    word_to_translate = input('Type the word you want to translate:\n')
    print()

    return language_from, language_to, word_to_translate


def get_response(src_lang: str, trg_lang: str, word: str) -> requests.Response:
    """
    Return the Response object
    :src_lang : source language
    :trg_lang : target language
    :word : words to translate
    :returns : Response
    """
    url = f'https://context.reverso.net/translation/{src_lang}-{trg_lang}/{word}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    return response


def check_response(response: requests.Response) -> tuple[int, str]:
    """
    Return status code and status of the given response
    :response : requests.Response
    :returns : tuple of status code and status
    """
    if response.ok:
        return response.status_code, 'OK'
    return response.status_code, 'Failed'


def pull_data(response: requests.Response) -> tuple[list[str], list[str], list[str]]:
    """
    Pulls the words and sentences from the given Response
    :response : requests.Response
    :returns : tuple of three lists: [words], [source_sentences], [target_sentences]
    """
    soup = BeautifulSoup(response.text, 'html.parser')
    words = [word.text.strip() for word in soup.find(id='translations-content').find_all('a')]
    source_sentences = [sentence.text.strip()
                        for sentence
                        in soup.find(id='examples-content').find_all('div', {'class': 'src ltr'})]
    target_sentences = [sentence.text.strip()
                        for sentence
                        in soup.find(id='examples-content').find_all('div', {'class': 'trg ltr'})]
    return words, source_sentences, target_sentences


def output_translations(
        language: str, words: list[str],
        source_sentences: list[str],
        target_sentences: list[str]
        ) -> None:
    """
    Outputs the translations to the console in the fancy way
    """
    print(f'{language.capitalize()} Translations:')
    print(*words, sep='\n')
    print()
    print(f'{language.capitalize()} Examples:')
    for source, target in zip(source_sentences, target_sentences):
        print(source + ':', target, sep='\n', end='\n')
        print()


if __name__ == '__main__':
    main()
    # status_code, status = check_response(response)
    # print(f'You chose "{target_language}" as a language to translate "{word_to_translate}".')
    # print(status_code, status)
