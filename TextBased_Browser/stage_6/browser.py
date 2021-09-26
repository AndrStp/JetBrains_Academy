import os
from sys import argv
from typing import Optional
import requests
from bs4 import BeautifulSoup
from colorama import Fore


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
        page = get_web_page(url)
        if not page:
            print('Error: Incorrect URL')

        else:
            content = extract_content(page)
            save_to_dir(directory, name, content)
            print(content)
            stack.append(content)


def save_to_dir(directory: str, name: str, content: str) -> None:
    """Writes a content to a file"""
    full_path = os.path.join(directory, name)
    with open(full_path, 'w', encoding='UTF-8') as f:
        f.write(content)


def get_web_page(url: str) -> Optional[requests.models.Response]:
    """Return the text-content of a web page.
    None if request has failed"""
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/70.0.3538.77 Safari/537.36"
    try:
        r = requests.get(url, headers={'User-Agent': user_agent})
    except requests.exceptions.RequestException as e:
        return None
    return r


def extract_content(response: requests.models.Response) -> str:
    """Return the parsed content from the given page"""
    soup = BeautifulSoup(response.text, 'html.parser')
    tags = ['title', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']
    content = []
    for tag in soup.find_all(tags):
        text = tag.get_text()
        if tag.name == 'a':
            text = Fore.BLUE + tag.get_text() + Fore.RESET
        content.append(text)
    return '\n'.join(content)


if __name__ == '__main__':
    main()
