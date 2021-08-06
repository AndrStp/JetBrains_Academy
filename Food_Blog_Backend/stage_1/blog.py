import sqlite3
import sys


args = sys.argv
DB = args[1]

conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute("""CREATE TABLE meals (
                meal_id INT PRIMARY KEY,
                meal_name TEXT UNIQUE NOT NULL
                );
            """)

cur.execute("""CREATE TABLE ingredients (
                ingredient_id INT PRIMARY KEY,
                ingredient_name TEXT UNIQUE NOT NULL
                );
            """)

cur.execute("""CREATE TABLE measures (
                measure_id INT PRIMARY KEY,
                measure_name TEXT
                );
            """)


data = {
    "meals": ("breakfast", "brunch", "lunch", "supper"),
    "ingredients": ("milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
    "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")
}

for table in data.keys():
    for i, value in enumerate(data.get(table), start=1):
        cur.execute(f'INSERT INTO {table} VALUES (?, ?)', (i, value))

conn.commit()
conn.close()

print('The values have been added to', DB)
