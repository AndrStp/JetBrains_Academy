import requests


def main():
    curr_num = get_all_curr()  # 149 currencies total
    curr_in = input().lower()
    all_rates = {curr_in: get_default_rates(curr_in)}
    for i in range(curr_num):
        curr_out = input().lower()
        # if no input - exit
        if not curr_out:
            return
        amount = int(input())
        print('Checking the cache...')
        check = check_base(curr_in, curr_out, all_rates)
        if check:
            print('Oh! It is in the cache!')
        else:
            print('Sorry, but it is not in the cache!')
            all_rates[curr_in].update(get_exchange_rate(curr_in, curr_out))
        print(f'You received {calc_ex(amount, all_rates, curr_out, curr_in)} {curr_out.upper()}.')


def get_exchange_rate(curr_in: str, curr_out: str) -> dict:
    """Retrieve info from the url and return the exchange rates for curr_in into curr_out"""
    url = f'http://www.floatrates.com/daily/{curr_in}.json'
    json_dict = requests.get(url).json()
    rates = {curr_out: json_dict.get(curr_out).get('rate')}
    return rates


def get_default_rates(currency: str) -> dict:
    """Retrieve info from the url and return the exchange rates for currency into USD and EUR"""
    url = f'http://www.floatrates.com/daily/{currency}.json'
    json_dict = requests.get(url).json()
    if currency == 'usd':
        rates = {'eur': json_dict.get('eur').get('rate')}
    elif currency == 'eur':
        rates = {'usd': json_dict.get('usd').get('rate')}
    else:
        rates = {'usd': json_dict.get('usd').get('rate'), 'eur': json_dict.get('eur').get('rate')}
    return rates


def check_base(curr_in: str, curr_out: str, base: dict) -> bool:
    """Return whether the currency is in the cache"""
    if not base.get(curr_in) or curr_out not in base.get(curr_in):
        return False
    else:
        return True


def calc_ex(amount: int, base: dict, curr_out: str, curr_in: str) -> float:
    """Returns the sum following the exchange"""
    amount_out = amount * base.get(curr_in).get(curr_out)
    # return f'amount: {amount}, base: {base}, curr_out: {curr_out}, curr_in: {curr_in}'
    return round(amount_out, 2)


def get_all_curr():
    """Returns the list of all currencies in json"""
    r = requests.get('http://www.floatrates.com/daily/usd.json').json()
    return len(r.keys())


if __name__ == '__main__':
    main()
