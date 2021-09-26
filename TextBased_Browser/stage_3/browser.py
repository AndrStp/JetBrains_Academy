import os
from sys import argv
from typing import Tuple


nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

web_sites = {'nytimes': nytimes_com, 'bloomberg': bloomberg_com}

def main(db: dict) -> None:
    args = argv
    directory = args[1]

    if not os.access(directory, os.F_OK):
        os.mkdir(directory)

    stack = []
    while True:
        name, domain = read_input()
        if name == 'exit':
            break

        content = web_sites.get(name)
        if not content:
            print('Error: Incorrect URL')
        else:
            save_to_dir(directory, name, content)
            print(content)
            stack.append(content)

        if name == 'back':
            stack.pop()
            try:
                print(stack.pop())
            except IndexError:
                pass


def read_input() -> Tuple[str, list]:
    """Returns the tuple with website name and a domain"""
    name, *domain = input().split('.')
    return name, domain


def save_to_dir(directory: str, name: str, content: str) -> None:
    """Writes a content to a file"""
    full_path = os.path.join(directory, name)
    with open(full_path, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    main(web_sites)
