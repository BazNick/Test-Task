import os
import sqlite3

query = """
           CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               second_name TEXT,
               first_name TEXT,
               patronymic TEXT,
               region_id INTEGER,
               city_id INTEGER,
               phone TEXT,
               email TEXT,
               FOREIGN KEY (region_id) REFERENCES regions (id),
               FOREIGN KEY (city_id) REFERENCES cities (id)
           );

           CREATE TABLE IF NOT EXISTS regions (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               region_name TEXT
           );

           CREATE TABLE IF NOT EXISTS cities (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               region_id INTEGER, 
               city_name TEXT,
               FOREIGN KEY (region_id) REFERENCES regions (id)
           );

           INSERT INTO users (second_name, first_name, patronymic, region_id, city_id, phone, email) 
           VALUES 
           (
              'Крайзенберг', 'Петр', 'Романович', 3, 9, '8 (915) 781-12-45', 'kraizenberg_petr@mail.ru'
           ),
           
           (
              'Иванова', 'Анна', 'Ивановна', 0, 2, '8 (999) 555-55-55', 'ivanova-ann@yandex.ru'
           );

           INSERT INTO regions (id, region_name)
           VALUES 
              (0, 'Краснодарский край'),
              (1, 'Ростовская область'),
              (2, 'Ставропольский край');

           INSERT INTO cities (id, region_id, city_name) 
           VALUES 
              (0, 0, 'Краснодар'),
              (1, 0, 'Кропоткин'),
              (2, 0, 'Славянск'),
              (3, 1, 'Ростов'),
              (4, 1, 'Шахты'),
              (5, 1, 'Батайск'),
              (6, 2, 'Ставрополь'),
              (7, 2, 'Пятигорск'),
              (8, 2, 'Кисловодск');

           INSERT INTO regions (region_name)
           VALUES 
              ('Московская область');

           INSERT INTO cities (region_id, city_name)
           VALUES 
              (3, 'Москва');   
                      
       """


def execute_query(script):
    if os.path.exists('./task.sqlite'):
        cursor = sqlite3.connect('task.sqlite').cursor()
        print('----------- Cities Table Data -----------')
        for city in cursor.execute("SELECT * FROM cities"):
            print(city)
        print('\n')
        print('----------- Regions Table Data -----------')
        for region in cursor.execute("SELECT * FROM regions"):
            print(region)
        print('\n')
        print('----------- Users Table Data -----------')
        for user in cursor.execute("SELECT * FROM users"):
            print(user)
    else:
        create_db = sqlite3.connect('task.sqlite')
        with create_db as db:
            cursor = db.cursor()
            cursor.executescript(script)


execute_query(query)
