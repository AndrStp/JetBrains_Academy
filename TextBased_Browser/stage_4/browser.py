import os
from sys import argv
from typing import Optional
import requests
from bs4 import BeautifulSoup


def main() -> None:
    args = argv
    directory = args[1]

    if not os.access(directory, os.F_OK):
        os.mkdir(directory)

    stack = []
    while True:
        choice = input()
        if choice == 'exit':
            break

        if choice == 'back':
            stack.pop()
            try:
                print(stack.pop())
            except IndexError:
                pass

        name = choice.split('.')[0]
        url = 'https://' + choice
        content = get_web_page_content(url)
        if not content:
            print('Error: Incorrect URL')
        else:
            save_to_dir(directory, name, content)
            print(content)
            stack.append(content)


def save_to_dir(directory: str, name: str, content: str) -> None:
    """Writes a content to a file"""
    full_path = os.path.join(directory, name)
    with open(full_path, 'w', encoding='UTF-8') as f:
        f.write(content)


def get_web_page_content(url: str) -> Optional[str]:
    """Return the text-content of a web page.
    None if request has failed"""
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/70.0.3538.77 Safari/537.36"
    try:
        r = requests.get(url, headers={'User-Agent': user_agent})
    except requests.exceptions.RequestException as e:
        return None
    return r.text




if __name__ == '__main__':
    main()

# def read_input() -> Tuple[str, list]:
#     """Returns the tuple with website name and a domain"""
#     name, *domain = input().split('.')
#     return name, domain
