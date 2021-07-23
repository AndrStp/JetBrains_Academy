# write your code here

def main():
    """Runs the script"""
    formatters = ['plain', 'bold', 'italic', 'inline-code', 'link', 'header', 'new-line']
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
            flag = False


def use_formatting(formatter: str) -> str:
    """Return the text with formatting applied"""
    global formatted_text
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
    flag = True
    global level
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


if __name__ == '__main__':
    main()
