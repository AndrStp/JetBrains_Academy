import requests


def main():
    quote = get_quote()
    print(quote)


def get_quote():
    """Return the quote by the given URL"""
    query = input('Input the URL:\n')
    try:
        r = requests.get(query)
        if r.status_code == 200:
            r_json = r.json()
            return r_json['content']
        else:
            return 'Invalid quote resource!'
    except KeyError:
        return 'Invalid quote resource!'


if __name__ == '__main__':
    main()
