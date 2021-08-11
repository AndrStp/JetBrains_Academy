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
    print('Pass the empty recipe name to exit.')
    while True:
        recipe_name, recipe_desc = take_recipes()
        if not recipe_name:
            quit()
        populate_recipes(conn, recipe_name, recipe_desc)
        meals = get_meals(conn)
        display_meals(meals)
        when_served = [int(x) for x in input('When the dish can be served: ').split()]
        recipe_id = get_recipe_id(conn, recipe_name)
        populate_serve(conn, when_served, recipe_id)
        while True:
            qnt_msr_igrdnt = get_qnt_msr_igrdnt()
            if not qnt_msr_igrdnt:
                break
            quantity = qnt_msr_igrdnt[0]
            measure_id, ingredient_id = get_msr_ingrdnt_ids(conn, qnt_msr_igrdnt)
            populate_quantity(conn, quantity, recipe_id, measure_id, ingredient_id)


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

        connection.execute("""CREATE TABLE IF NOT EXISTS quantity (
                        quantity_id INTEGER PRIMARY KEY,
                        quantity INTEGER NOT NULL,
                        recipe_id INTEGER NOT NULL,
                        measure_id INTEGER NOT NULL,
                        ingredient_id INTEGER NOT NULL,
                        FOREIGN KEY (recipe_id) REFERENCES recipes (recipe_id),
                        FOREIGN KEY (measure_id) REFERENCES measures (measure_id),
                        FOREIGN KEY (ingredient_id) REFERENCES ingredients (ingredient_id)
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
    recipe_name = input('Recipe name: ')
    if not recipe_name:
        return None, None
    recipe_desc = input('Recipe description: ')
    return recipe_name, recipe_desc


def populate_recipes(connection, recipe_name: str, recipe_desc: str) -> None:
    """Populates the recipe table with user provided data"""
    with connection:
        connection.execute('INSERT INTO recipes (recipe_name, recipe_description) VALUES (?, ?)', (recipe_name, recipe_desc))


def populate_serve(connection, meals: list, recipe_id: str) -> None:
    """Populates serve table"""
    with connection:
        for meal in meals:
            connection.execute('INSERT INTO serve (meal_id, recipe_id) VALUES (?, ?)', (meal, recipe_id))


def get_recipe_id(connection, recipe_name: str) -> str:
    """Return recipe_id of the given recipe_name"""
    with connection:
        return connection.execute('SELECT recipe_id FROM recipes WHERE recipe_name=?', (recipe_name,)).fetchone()[0]


def get_msr_ingrdnt_ids(connection, qnt_msr_igrdnt: tuple) -> tuple:
    """Return the measure and ingredient ids from the respective tables"""
    with connection:
        measure_id = connection.execute('SELECT measure_id FROM measures WHERE measure_name=?', (qnt_msr_igrdnt[1],)).fetchone()
        ingredient_id = connection.execute('SELECT ingredient_id FROM ingredients WHERE ingredient_name=?', (qnt_msr_igrdnt[2],)).fetchone()
    return measure_id[0], ingredient_id[0]


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


def get_qnt_msr_igrdnt() -> tuple or None:
    """Return tuple (quantity, measure, ingredient) or None"""
    while True:
        ingred_input = input('Input quantity of ingredient <press enter to stop>: ').split()
        if not ingred_input:
            return None
        if len(ingred_input) > 2:
            quantity, measure, ingrdnt = ingred_input
            possible_measure = [measure_ for measure_ in DATA['measures'] if measure_.startswith(measure)]
            if len(possible_measure) > 1 and measure not in DATA['measures']:
                print('The measure is not conclusive!')
                continue
            else:
                measure = possible_measure[0]

        else:
            quantity, ingrdnt = ingred_input
            measure = ''

        possible_ingrdnt = [ingredient for ingredient in DATA['ingredients'] if ingredient.startswith(ingrdnt)]

        if len(possible_ingrdnt) > 1 and ingrdnt not in DATA['ingredients']:
            print('The ingredient is not conclusive!')
            continue
        else:
            ingrdnt = possible_ingrdnt[0]

        return quantity, measure, ingrdnt


def populate_quantity(connection, quantity: str, recipe_id: str, measure_id: str, ingredient_id: str) -> None:
    """Populates the quantity table"""
    with connection:
        connection.execute("""INSERT INTO quantity 
                            (quantity, recipe_id, measure_id, ingredient_id) 
                            VALUES (?, ?, ?, ?)""", (quantity, recipe_id, measure_id, ingredient_id))


if __name__ == '__main__':
    main()
