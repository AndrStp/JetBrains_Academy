import sqlite3
import sys


args = sys.argv
DB = args[1]

data = {
    "meals": ("breakfast", "brunch", "lunch", "supper"),
    "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
    "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")
}


def main():
    create_tables()
    populate_tables()
    populate_recipes()


def create_tables():
    """Creates required tables"""
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE recipes (
                    recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipe_name TEXT NOT NULL,
                    recipe_description TEXT
                    );
                """)

    cur.execute("""CREATE TABLE meals (
                    meal_id INTEGER PRIMARY KEY,
                    meal_name TEXT UNIQUE NOT NULL
                    );
                """)

    cur.execute("""CREATE TABLE ingredients (
                    ingredient_id INTEGER PRIMARY KEY,
                    ingredient_name TEXT UNIQUE NOT NULL
                    );
                """)

    cur.execute("""CREATE TABLE measures (
                    measure_id INTEGER PRIMARY KEY,
                    measure_name TEXT
                    );
                """)

    conn.commit()
    conn.close()
    print('Created tables in', DB)


def populate_tables():
    """Populates all tables from stage_1"""
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    for table in data.keys():
        for i, value in enumerate(data.get(table), start=1):
            cur.execute(f'INSERT INTO {table} VALUES (?, ?)', (i, value))

    conn.commit()
    conn.close()
    print('The values have been added to tables from stage_1 of', DB)


def populate_recipes():
    """Populates the recipe table with user provided data"""
    connection = sqlite3.connect(DB)
    curs = connection.cursor()

    print('Pass the empty recipe name to exit.')
    i = 0
    while True:
        recipe_name = input('Recipe name: ')
        if not recipe_name:
            break
        recipe_desc = input('Recipe description: ')
        curs.execute('INSERT INTO recipes (recipe_name, recipe_description) VALUES (?, ?)', (recipe_name, recipe_desc))

    connection.commit()
    connection.close()
    print('The values have been added to table recipes of', DB)


if __name__ == '__main__':
    main()
