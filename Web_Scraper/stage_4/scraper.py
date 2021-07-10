import requests
from bs4 import BeautifulSoup
import string


def main():
    query = 'https://www.nature.com/nature/articles'
    title_url_pairs = get_title_url_pairs(query)
    processed = process_titles(title_url_pairs)
    contents = get_contents(title_url_pairs)
    save_to_file(processed, contents)
    print('Saved articles: ', display_message(processed), sep='\n')


def get_title_url_pairs(query: str) -> dict:
    """Return the list of articles titles"""
    title_url_pairs = dict()
    r = requests.get(query)
    soup = BeautifulSoup(r.content, 'html.parser')
    articles = soup.find_all('article', class_='u-full-height c-card c-card--flush')
    for position in articles:
        meta_block = position.find('div', class_='c-card__section c-meta')
        category = meta_block.span.span.text
        if category == 'News':
            body_block = position.find('div', class_='c-card__layout u-full-height')
            title = body_block.a.text
            url = 'https://www.nature.com' + body_block.a.get('href')
            title_url_pairs[title] = url
    return title_url_pairs


def get_contents(data: dict) -> list:
    """Returns the list of contents of the articles"""
    pages_text = []
    for url in data.values():
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
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


def save_to_file(titles: list, contents: list):
    """Write content of a article to separate file"""
    for title, content in zip(titles, contents):
        with open(f'{title}.txt', 'w', encoding='utf-8') as f:
            f.write(content)


def display_message(titles: list):
    names = []
    for title in titles:
        name = title + '.txt'
        names.append(name)
    return names


if __name__ == '__main__':
    main()


# div class_='c-article-body u-clearfix'
