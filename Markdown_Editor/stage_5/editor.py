# write your code here

def main():
    """Runs the script"""
    formatters = ['plain', 'bold', 'italic', 'inline-code', 'link', 'header',
                  'new-line', 'ordered-list', 'unordered-list']
    commands = ['!help', '!done']
    
    text = ''
    flag = True
    while flag:
        request = input('Choose a formatter: ')
        if request not in formatters and request not in commands:
            print('Unknown formatting type or command')
        elif request in formatters:
            formatted_text = use_formatting(request)
            text += formatted_text
            print(text)
        elif request == '!help':
            print('Available formatters:', ' '.join(formatters))
            print('Special commands:', ' '.join(commands))
        elif request == '!done':
            with open('output.md', 'w', encoding='utf-8') as output:
                output.write(text)
                flag = False


def use_formatting(formatter: str) -> str:
    """Return the text with formatting applied"""
    formatted_text = None
    if formatter == 'plain':
        formatted_text = apply_plain()
    elif formatter == 'bold':
        formatted_text = apply_bold()
    elif formatter == 'italic':
        formatted_text = apply_italic()
    elif formatter == 'inline-code':
        formatted_text = apply_inline_code()
    elif formatter == 'link':
        formatted_text = apply_link()
    elif formatter == 'header':
        formatted_text = apply_header()
    elif formatter == 'new-line':
        formatted_text = apply_new_line()
    elif formatter in ['ordered-list', 'unordered-list']:
        formatter = formatter.split(sep='-')[0]
        formatted_text = apply_list(formatter)
    return formatted_text


def apply_plain() -> str:
    """Returns plain text"""
    text = input('Text: ')
    return text


def apply_bold() -> str:
    """Returns bold text"""
    text = input('Text: ')
    return f'**{text}**'


def apply_italic() -> str:
    """Returns italic text"""
    text = input('Text: ')
    return f'*{text}*'


def apply_inline_code() -> str:
    """Returns inline_code-like text"""
    text = input('Text: ')
    return f'`{text}`'


def apply_link() -> str:
    """Returns link-like text"""
    text = input('Label: ')
    link = input('URL: ')
    return f'[{text}]({link})'


def apply_header() -> str:
    """Returns heads-like text with the given level"""
    level = None
    flag = True
    while flag:
        level = int(input('Level: '))
        if level > 6:
            print('The level should be within the range of 1 to 6')
        else:
            flag = False
    text = input('Text: ')
    return '#' * level + ' ' + text + '\n'


def apply_new_line() -> str:
    """Returns new-line character"""
    return '\n'


def apply_list(list_type: str) -> str:
    """Returns a list" of a given type (ordered/unordered)"""
    text = []
    n_rows = None
    flag = True
    while flag:
        n_rows = int(input('Number of rows: '))
        if n_rows < 1:
            print('The number of rows should be greater than zero')
            continue
        else:
            flag = False
    for i in range(n_rows):
        row = input(f'Row #{i + 1}: ')
        if list_type == 'ordered':
            text.append(f'{i + 1}. {row}')
        else:
            text.append('* ' + row)
    return '\n'.join(text) + '\n'


if __name__ == '__main__':
    main()
