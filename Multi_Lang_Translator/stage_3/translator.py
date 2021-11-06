import requests
from bs4 import BeautifulSoup


def main():
    target_language, word_to_translate = take_args()
    response = get_response(target_language, word_to_translate)
    status_code, status = check_response(response)

    print(f'You chose "{target_language}" as a language to translate "{word_to_translate}".')
    print(status_code, status)

    words, sentences = pull_data(response)
    output_translations(target_language, words, sentences)


def take_args() -> tuple[str, str]:
    """
    Return args from the user
    :return tuple of target language and word
    """
    language = input('Type "en" if you want to translate from French into English, ' +
                     'or "fr" if you want to translate from English into French:\n')
    word_to_translate = input('Type the word you want to translate:\n')

    return language, word_to_translate


def get_response(lang: str, word: str) -> requests.Response:
    """
    Return the Response object
    :lang : target language
    :word : words to translate
    :returns : Response
    """
    if lang == 'en':
        lang_to = 'english'
        lang_from = 'french'
    else:
        lang_to = 'french'
        lang_from = 'english'

    url = f'https://context.reverso.net/translation/{lang_from}-{lang_to}/{word}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=headers)
    return r


def check_response(r: requests.Response) -> tuple[int, str]:
    """
    Return status code and status of the given response
    :r : requests.Response
    :returns : tuple of status code and status
    """
    if r.ok:
        return r.status_code, 'OK'
    return r.status_code, 'Failed'


def pull_data(r: requests.Response) -> tuple[list[str], list[str]]:
    """
    Pulls the words and sentences from the given Response
    :r : requests.Response
    :returns : tuple of two lists: [words], [sentences]
    """
    soup = BeautifulSoup(r.text, 'html.parser')
    words = [word.text.strip()
             for word in soup.find(id='translations-content').select('a')]
    sentences = [sentence.text.strip()
                 for sentence in soup.find(id="examples-content").select(".ltr")]
    return words, sentences


def output_translations(language: str, words: list[str], sentences: list[str]) -> None:
    """Outputs the translations to the console in the fancy way"""
    lang = None
    if language == 'fr':
        lang = 'French'
    else:
        lang = 'English'

    print(f'{lang} Translation:')
    print(*words, sep='\n')
    print()
    print(f'{lang} Examples:')
    print(*sentences, sep='\n')



if __name__ == '__main__':
    main()
