import requests
from bs4 import BeautifulSoup
import json


def main():
    query = input('Input the URL:\n')
    # query = 'https://www.imdb.com/title/tt0080684/'
    media = get_imdb(query)
    print()
    print(media)


def get_imdb(query: str):
    """Return the quote by the given URL"""
    try:
        r = requests.get(query, headers={'Accept-Language': 'en-US,en;q=0.5'})
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            script_tag = soup.find("script", type="application/ld+json")
            if not script_tag:
                return 'Invalid movie page!'
            data = json.loads(''.join(script_tag))
            if data['@type'] not in ['Movie', 'TVSeries']:
                return 'Invalid movie page!'
            else:
                movie_data = {
                    'title': data['name'],
                    'description': data['description'].split('.')[1].strip()
                }
                return movie_data
        else:
            return 'Invalid movie page!'
    except KeyError:
        return 'Invalid movie page!'


if __name__ == '__main__':
    main()
