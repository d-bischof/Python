import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import random

cities = [
    {"city": "Jacksonville", "year": 2025, "population": 1024310},
    {"city": "Miami", "year": 2025, "population": 498060},
    {"city": "Tampa", "year": 2025, "population": 421042},
    {"city": "Orlando", "year": 2025, "population": 341600},
    {"city": "Port St. Lucie", "year": 2025, "population": 271511},
    {"city": "St. Petersburg", "year": 2025, "population": 269059},
    {"city": "Cape Coral", "year": 2025, "population": 242422},
    {"city": "Hialeah", "year": 2025, "population": 238630},
    {"city": "Tallahassee", "year": 2025, "population": 206877},
    {"city": "Fort Lauderdale", "year": 2025, "population": 192610}
]

def create_database():

    # connect to the SQLite database file and get a cursor for SQL commands
    connection = sqlite3.connect("population_DB.db")
    cursor = connection.cursor()

    # create the table if it does not already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT NOT NULL,
            year INTEGER NOT NULL,
            population INTEGER NOT NULL
        )
    ''')

    cursor.execute("DELETE FROM population")

    # insert all sample city rows into the table
    query = "INSERT INTO population (city, year, population) VALUES (:city, :year, :population)"

    cursor.executemany(query, cities)

    #print(pd.read_sql_query("SELECT * FROM population", connection))

    connection.commit()
    connection.close()



def simulate_population_growth(years=20):

    # open the database again to add projected population data
    connection = sqlite3.connect("population_DB.db")
    cursor = connection.cursor()

    cursor.execute("SELECT DISTINCT city FROM population")
    cities = cursor.fetchall()

    for list in cities:
        city = list[0]

        cursor.execute('SELECT population FROM population WHERE city = ? AND year = 2025', (city,))

        result = cursor.fetchone()

        if result:
            population = result[0]

            for year in range(2026, 2026 + years):

                # simulate a small annual growth or decline randomly
                growth_rate = random.uniform(-0.01, 0.02)
                population = int(population * (1 + growth_rate))

                cursor.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)", (city, year, population))

    print()

    #print(pd.read_sql_query("SELECT * FROM population", connection))

    connection.commit()
    connection.close()

def display_city_growth():
    # show a list of cities and ask the user which one to plot
    connection = sqlite3.connect("population_DB.db")
    cursor = connection.cursor()

    names = [d["city"] for d in cities]

    print('\n'.join(names))
    print()

    x: str = ""
    index: int = 0

    while(True):
        x = input("Please enter one of the following cities: ")

        for i, name in enumerate(names):
            if name.lower() == x.lower():
                index = i
                break

        if index != 0:
            break
        else:
            print(f"no matches for {x} in cities")

    print(f"your city choice is {names[index]}")

    df = pd.read_sql_query("SELECT * FROM population WHERE city = ? ORDER BY year", connection, params=[names[index]])

    plt.figure(figsize=(10, 6))
    plt.plot(df['year'], df['population'], marker='o', linewidth=2, markersize=6)
    plt.xticks(df['year'][::3], rotation=45)
    plt.title(f'Population Growth: {names[index]}', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Population', fontsize=12, labelpad = 20)
    plt.grid(True, alpha=0.3)
    plt.show()


def main():
    create_database()
    simulate_population_growth()
    display_city_growth()

if __name__ == '__main__':
    main()
