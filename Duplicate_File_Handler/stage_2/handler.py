import os
import sys
import typing


def main():
    directory = read_cli()
    if directory is None:
        print('Directory is not specified')
        return
    file_ext, sort_option = read_input()
    grouped = sorting_files(directory, file_ext)
    display_files(grouped, sort_option)


def read_input() -> tuple:
    """Returns the file format and the size sorting option"""
    f_format = input('Enter file format:\n')
    print()
    print('Size sorting options:',
          '1. Descending',
          '2. Ascending\n', sep='\n')
    while True:
        option = input('Enter a sorting option:\n')
        print()
        if option in ['1', '2']:
            return f_format, option
        else:
            print('Wrong option\n')


def read_cli() -> typing.Union[str, None]:
    """Returns the directory or None if no directory is provided"""
    args = sys.argv
    if len(args) < 2:
        return None
    return args[1]


def sorting_files(directory: str, file_ext: str) -> dict:
    """Return the dict of files grouped by the size"""
    files = dict()
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            f_name, f_ext = os.path.splitext(filename)
            if file_ext == f_ext.lstrip('.') or file_ext == '':
                path_to_file = os.path.join(dirpath, filename)
                f_size = os.path.getsize(path_to_file)
                files.setdefault(f_size, []).append(path_to_file)
    return files


def display_files(files: dict, sort_opt: str):
    """Displays the files either in descending (1) or ascending (2) order"""
    if sort_opt == '1':
        for f_size in sorted(files.keys(), reverse=True):
            print(f_size, 'bytes')
            for f_name in files[f_size]:
                print(f_name)
            print()
    else:
        for f_size in sorted(files.keys()):
            print(f_size, 'bytes')
            for f_name in files[f_size]:
                print(f_name)
            print()


if __name__ == '__main__':
    main()
