import psycopg2
import creating
import inserting
import selecting
import showing

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="qwer1234",
    host="localhost",
    port="5432")

cursor = conn.cursor()
creating.delete_db(cursor)
creating.create_db(cursor)

print("Для получения дополнительной информации введите \"СПРАВКА\"")
while True:
    command = input('Введите команду:')
    if command == "СПРАВКА":
        print("Для работы с базой вы можете использовать следующие команды\n"
              "ДОБАВИТЬ-внести видео в базу данных\n"
              "ПОИСК-поиск по базе данных\n"
              "ПОКАЗАТЬ-показать все записи в базе данных\n"
              "ВЫХОД-остановить работу базы данных(ВНЕСЕННЫЕ ИЗМЕНЕНИЯ НЕ СОХРАНЯЮТСЯ!)")
    elif command == "ДОБАВИТЬ":
        inserting.get_insert_information(cursor)
        conn.commit()
    elif command == "ПОИСК":
        selecting.get_select_information(cursor)
        conn.commit()
    elif command == "ПОКАЗАТЬ":
        showing.show_video(cursor)
    elif command == "ВЫХОД":
        break
    else:
        print("Неизвестная команда, повторите попытку:")
conn.close()
print("Соединение завершено")
