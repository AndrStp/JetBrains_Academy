import requests
from bs4 import BeautifulSoup


def main():
    query = input('Input the URL:\n')
    code = get_webpage(query)
    if isinstance(code, int):
        print(f'\nThe URL returned {code}!')
    else:
        save_to_file(code)
        print('\nContent saved.')


def get_webpage(query: str):
    """Return the quote by the given URL"""
    r = requests.get(query)
    if r.status_code == 200:
        page_content = r.content
        return page_content
    else:
        return r.status_code


def save_to_file(page):
    with open('source.html', 'wb') as f:
        f.write(page)


if __name__ == '__main__':
    main()
