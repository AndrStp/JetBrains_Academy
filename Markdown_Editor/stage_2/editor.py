# write your code here

def main():
    """Runs the script"""
    formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code',
                  'ordered-list', 'unordered-list', 'new-line']
    commands = {
        '!help': f'Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line\
    \nSpecial commands: !help !done',
        '!done': 'exit'
    }
    flag = True
    while flag:
        request = input('Choose a formatter: ')
        if request not in formatters and request not in commands:
            print('Unknown formatting type or command')
        elif request in formatters:
            pass
        elif request in commands and request != '!done':
            print(commands[request])
        elif request == '!done':
            flag = False


main()
