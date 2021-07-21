import os
import sys
import typing
import hashlib


def main():
    directory = read_cli()
    if directory is None:
        print('Directory is not specified')
        return
    file_ext, sort_option = read_input()
    grouped = sorting_files(directory, file_ext)
    display_files(grouped, sort_option)
    check = input('Check for duplicates?\n')
    if check.lower() in ['yes', 'y']:
        print()
        duplicates = find_duplicates(grouped)
        display_duplicates(duplicates, sort_option)


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
            f_ext = os.path.splitext(filename)[-1]
            if file_ext == f_ext.lstrip('.') or file_ext == '':
                path_to_file = os.path.join(dirpath, filename)
                f_size = os.path.getsize(path_to_file)
                files.setdefault(f_size, []).append(path_to_file)
    return files


def find_duplicates(files: dict) -> dict:
    """Returns the dictionary of duplicate files with their hash"""
    duplicates = {}
    for f_size, f_array in files.items():
        # if we have one item of specific size skip it (no duplicates possible)
        if len(files[f_size]) < 2:
            continue
        temp = {}
        for file in f_array:
            with open(file, 'rb') as handle:
                content = handle.read()
                m = hashlib.md5()
                m.update(content)
                hash_value = m.hexdigest()
                temp.setdefault(hash_value, []).append(file)
        duplicate_hash_files = {key:value for key, value in temp.items() if len(value) > 1}
        duplicates[f_size] = duplicate_hash_files
    return duplicates


def display_files(files: dict, sort_opt: str):
    """Displays the files either in descending (1) or ascending (2) order"""
    if sort_opt == '1':
        files_keys = sorted(files.keys(), reverse=True)
    else:
        files_keys = sorted(files.keys())
    for f_size in files_keys:
        print(f_size, 'bytes')
        for f_name in files[f_size]:
            print(f_name)
        print()


def display_duplicates(files: dict, sort_opt: str):
    """Displays the duplicate files either in descending (1) or ascending (2) order and enumerates them"""
    counter = 1
    if sort_opt == '1':
        files_keys = sorted(files.keys(), reverse=True)
    else:
        files_keys = sorted(files.keys())
    for f_size in files_keys:
        print(f_size, 'bytes')
        for hash_value in files[f_size].keys():
            print('Hash:', hash_value)
            for f_name in files[f_size][hash_value]:
                print(counter, f_name, sep='. ')
                counter += 1
        print()


if __name__ == '__main__':
    main()
