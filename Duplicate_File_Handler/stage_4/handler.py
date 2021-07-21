import os
import sys
import typing
import hashlib


def main():
    directory = read_cli()
    if directory is None:
        print('Directory is not specified')
        return
    file_ext, sort_option = read_input_sorting()
    grouped = sorting_files(directory, file_ext)
    display_files(grouped, sort_option)
    dupl_opt = read_input_duplicates()
    if dupl_opt == 'yes':
        print()
        duplicates = find_duplicates(grouped)
        enum_files = display_duplicates(duplicates, sort_option)
        delete_opt = input('Delete files?\n')
        if delete_opt == 'yes':
            files_to_delete = process_delete_input(duplicates, enum_files)
            print()
            space = remove_files(files_to_delete)
            print('Total freed up space:', space, 'bytes')


def read_cli() -> typing.Union[str, None]:
    """Returns the directory or None if no directory is provided"""
    args = sys.argv
    if len(args) < 2:
        return None
    return args[1]


def read_input_sorting() -> tuple:
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


def read_input_duplicates() -> str:
    """Returns the string for finding duplicates (yes/no)"""
    while True:
        check = input('Check for duplicates?\n').lower()
        if check not in ['yes', 'no']:
            print('Wrong option')
            continue
        else:
            return check


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


def process_delete_input(files: dict, files_to_del: list) -> list:
    """Returns the list of numbers: str that should be deleted"""
    n_files = len(files_to_del)
    files_to_remove = []
    flag = True
    while flag:
        del_option = input('Enter file numbers to delete:\n').split()
        message = '\nWrong format\n'
        # check for empty sequence
        if not del_option:
            print(message)
            continue

        for i in del_option:
            # check for digits
            if not i.isdigit():
                print(message)
                continue
            # check for index
            elif int(i) not in range(1, n_files + 1):
                print(message)
                continue
            print(i)
            files_to_remove.append(files_to_del[int(i) - 1])
            flag = False
    return files_to_remove


def remove_files(files: list) -> int:
    """Remove the files specified in files: list. Returns the total amount of freed up space"""
    freed_space = 0
    for file in files:
        stat_info = os.stat(file)
        freed_space += stat_info.st_size
        os.remove(file)
    return freed_space


def display_files(files: dict, sort_opt: str) -> None:
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


def display_duplicates(files: dict, sort_opt: str) -> list:
    """Displays the duplicate files either in descending (1) or ascending (2) order and enumerates them.
    Returns the list of files names in the above specified order"""
    counter = 1
    counted_files = []
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
                counted_files.append(f_name)
                counter += 1
        print()
    return counted_files


if __name__ == '__main__':
    main()
