# Write your code here
import objects


def main():
    grid = objects.Grid()
    choice = input()
    print()
    print(grid)
    letter = objects.Letter(choice)
    letter.set_form()
    grid.take_letter(letter)
    grid.display_letter()


if __name__ == '__main__':
    main()
