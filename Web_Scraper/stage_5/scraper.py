import requests
from bs4 import BeautifulSoup
import string
import os


def main():
    query = 'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page='
    pages, page_type = read_input()
    for i in range(pages):
        title_url_pairs = get_title_url_pairs(query, str(i + 1), page_type)
        if title_url_pairs:
            contents = get_contents(title_url_pairs, page_type)
            processed = process_titles(title_url_pairs)
            save_to_file(processed, contents, i + 1)
        else:
            save_to_file(None, None, page_index=i + 1)
    print('Saved all articles.')


def read_input():
    """Returns the number of pages and type of pages"""
    p_indexes = int(input())
    p_type = input()
    return p_indexes, p_type


def get_title_url_pairs(query: str, p_index: str, p_type: str) -> dict:
    """Return the list of articles titles"""
    title_url_pairs = dict()
    r = requests.get(query + p_index)
    soup = BeautifulSoup(r.content, 'html.parser')
    articles = soup.find_all('article', class_='u-full-height c-card c-card--flush')
    for position in articles:
        meta_block = position.find('div', class_='c-card__section c-meta')
        category = meta_block.span.span.text
        if category == p_type:
            body_block = position.find('div', class_='c-card__layout u-full-height')
            title = body_block.a.text
            url = 'https://www.nature.com' + body_block.a.get('href')
            title_url_pairs[title] = url
    return title_url_pairs


def get_contents(data: dict, p_type: str) -> list:
    """Returns the list of contents of the articles"""
    pages_text = []
    for url in data.values():
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        if p_type == 'Research Highlight':
            page_content = soup.find('div', class_='article-item__body').text.strip()
        if p_type in ['News', 'News & Views', 'News Feature']:
            page_content = soup.find('div', class_='c-article-body u-clearfix').text.strip()
        pages_text.append(page_content)
    return pages_text


def process_titles(titles: dict) -> list:
    """Replaces the whitespaces with underscores and removes punctuation marks"""
    processed = []
    for title in list(titles.keys()):
        punctuation = string.punctuation
        mapping = str.maketrans('', '', punctuation)
        title_punctuation = title.translate(mapping)
        title_underscores = title_punctuation.translate(str.maketrans(' ', '_'))
        processed.append(title_underscores)
    return processed


def save_to_file(titles: list, contents: list, page_index: int):
    """Write content of page to a directory into a file"""
    project_dir = os.getcwd()
    page_folder = f'Page_{page_index}'
    new_dir = os.path.join(project_dir, page_folder)
    if not os.access(new_dir, os.F_OK):
        os.mkdir(page_folder)
    os.chdir(new_dir)
    if titles and contents:
        for title, content in zip(titles, contents):
            with open(f'{title}.txt', 'w', encoding='utf-8') as f:
                f.write(content)
    os.chdir(project_dir)


if __name__ == '__main__':
    main()

