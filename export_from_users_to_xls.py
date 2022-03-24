import os.path
import sqlite3
import regions_and_cities
import openpyxl


# Парсим данные из таблицы users
def parse_db(file):
    try:
        if os.path.exists(file):
            db = sqlite3.connect(file).cursor()
            users_list = []
            query = """
                SELECT * FROM users
            """
            for user in db.execute(query):
                users_list.append(user)

            return users_list
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        print('Файла БД еще не сформировано. Запустите сначала файл create_db.py')
    except Exception:
        print('Проверьте директорию на наличие файла')


# Функция преобразовывает столбцы таблицы users region_id и city_id из id в наименования
def parse_id_to_values(old_list, new_list, searching_dict, index):
    for k, v in searching_dict.items():
        for _tuple in old_list:
            if k == _tuple[index]:
                _tuple = list(_tuple)
                _tuple[index] = v
                _tuple = tuple(_tuple)
                new_list.append(_tuple)
    return new_list


def insert_to_xls(data, file):
    try:
        if data is None:
            raise TypeError
        # Открываем excel файл
        excel_file = openpyxl.load_workbook(file)
        active_sheet = excel_file.active
        last_row = active_sheet.max_row
        last_row_id_number = active_sheet[f'A{last_row}'].value

        # Берем последнее значение в excel файле из столбца id
        new_list = []
        for item in data:
            last_row_id_number += 1
            item = list(item)
            item[0] = last_row_id_number
            item = tuple(item)
            new_list.append(item)

        # Преобразовываем region_id из id в наименования
        another_list = []
        updated_region = parse_id_to_values(new_list, another_list, regions_and_cities.regions_dict, 4)

        # Преобразовываем city_id из id в наименования
        upd_cities_list = []
        final_list = parse_id_to_values(updated_region, upd_cities_list, regions_and_cities.cities_dict, 5)

        # Сортируем получившейся список
        final_list.sort()
        for item in final_list:
            active_sheet.append(item)
        excel_file.save('test_1.xlsx')
    except TypeError:
        print('Скорее всего файла БД еще не сформировано. Попробуйте запустить сначала файл create_db.py')
    except FileNotFoundError:
        print('Файла xlsx/xls не найдено. Пожалуйста, импортируйте Excel файл для работы.')


massive_data = parse_db('task.sqlite')
insert_to_xls(massive_data, 'test.xlsx')
