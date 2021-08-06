import sqlite3
import sys


args = sys.argv
DB = args[1]

DATA = {
    "meals": ("breakfast", "brunch", "lunch", "supper"),
    "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
    "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")
}


def main():
    conn = connect(DB)
    create_tables(conn)
    populate_tables(conn)
    while True:
        recipe_name, recipe_desc = take_recipes()
        if not recipe_name:
            quit()
        populate_recipes(conn, recipe_name, recipe_desc)
        meals = get_meals(conn)
        display_meals(meals)
        when_served = [int(x) for x in input('When the dish can be served: ').split()]
        populate_serve(conn, when_served, recipe_name)


def connect(db: str):
    """Return connection (cursor) to the db"""
    return sqlite3.connect(db)


def create_tables(connection) -> None:
    """Creates required tables"""
    with connection:
        connection.execute("PRAGMA foreign_keys = 1")

        connection.execute(f"""CREATE TABLE IF NOT EXISTS recipes (
                        recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        recipe_name TEXT NOT NULL,
                        recipe_description TEXT
                        );
                    """)

        connection.execute("""CREATE TABLE IF NOT EXISTS meals (
                        meal_id INTEGER PRIMARY KEY,
                        meal_name TEXT NOT NULL UNIQUE
                        );
                    """)

        connection.execute("""CREATE TABLE IF NOT EXISTS ingredients (
                        ingredient_id INTEGER PRIMARY KEY,
                        ingredient_name TEXT NOT NULL UNIQUE
                        );
                    """)

        connection.execute("""CREATE TABLE IF NOT EXISTS measures (
                        measure_id INTEGER PRIMARY KEY,
                        measure_name TEXT UNIQUE
                        );
                    """)

        connection.execute("""CREATE TABLE IF NOT EXISTS serve (
                        serve_id INTEGER PRIMARY KEY,
                        meal_id INTEGER NOT NULL,
                        recipe_id INTEGER NOT NULL,
                        FOREIGN KEY (meal_id) REFERENCES meals (meal_id),
                        FOREIGN KEY (recipe_id) REFERENCES recipes (recipe_id)    
                        );
                    """)


def populate_tables(connection) -> None:
    """Populates all tables from stage_1"""
    with connection:
        for table in DATA.keys():
            for i, value in enumerate(DATA.get(table), start=1):
                connection.execute(f'INSERT INTO {table} VALUES (?, ?)', (i, value))


def take_recipes() -> tuple:
    """Returns recipe_names and recipe_descs taken from the user"""
    print('Pass the empty recipe name to exit.')
    recipe_name = input('Recipe name: ')
    if not recipe_name:
        return None, None
    recipe_desc = input('Recipe description: ')
    return recipe_name, recipe_desc


def populate_recipes(connection, recipe_name: str, recipe_desc: str) -> None:
    """Populates the recipe table with user provided data"""
    with connection:
        connection.execute('INSERT INTO recipes (recipe_name, recipe_description) VALUES (?, ?)', (recipe_name, recipe_desc))


def populate_serve(connection, meals: list, recipe_name: str) -> None:
    """Populates serve table"""
    with connection:
        recipe_id = connection.execute('SELECT recipe_id FROM recipes WHERE recipe_name=?', (recipe_name,)).fetchone()
        print(recipe_id)
        for meal in meals:
            connection.execute('INSERT INTO serve (meal_id, recipe_id) VALUES (?, ?)', (meal, recipe_id[0]))


def get_meals(connection) -> list:
    """Return everything from meals table"""
    with connection:
        result = connection.execute("SELECT * FROM meals").fetchall()
    return result


def display_meals(meals: list) -> None:
    """Displays meal_id and meal_name in one line"""
    for index, meal in meals:
        print(f'{index}) {meal}', end=' ')
    print()


if __name__ == '__main__':
    main()
