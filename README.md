# Test-Task

Для того, чтобы работать с таблицами БД, необходимо сперва создать файл БД. Запустите файл ```create_db.py```, чтобы сформировать файл БД в текущей директории.

В проекте есть файл ```xlsx```, чтобы можно было проверить работоспособность проекта. ***!_Примечание_! Все данные в файле ```test.xlsx``` выдуманны.***

Файл ```import_from_xls_to_users.py``` позволяет импортировать данные из файла таблицы ```test.xlsx```, в таблицу ```users``` БД с правильным конвертированием наименованиев регионов и городов в виде ```id```.

Файл ```export_from_users_to_xls.py``` позволяет экспортировать данные из файла БД таблицы ```users```, в таблицу файла ```test.xlsx``` с правильным конвертированием ```id``` регионов и городов в их представление в виде наименований.
