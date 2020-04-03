import psycopg2
import re

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="qwer1234",
    host="localhost",
    port="5432")

cursor = conn.cursor()


def remake_db():
    cursor.execute("DROP TABLE artists")
    cursor.execute("DROP TABLE persons")
    cursor.execute("DROP TABLE countries")
    cursor.execute("DROP TABLE videos")
    cursor.execute("DROP TABLE genres")


def create_db():
    cursor.execute("CREATE TABLE artists(artist_id INT ," +
                   "country_id INT ," +
                   "video_id INT )")
    cursor.execute("CREATE TABLE persons(artist_id SERIAL PRIMARY KEY," +
                   "last_name VARCHAR(15) DEFAULT 'Undefined'," +
                   "nickname VARCHAR(15) DEFAULT 'Undefined'," +
                   "first_name VARCHAR(15) DEFAULT 'Undefined'," +
                   "birthday VARCHAR(15) DEFAULT 'Undefined'," +
                   "sex VARCHAR(10) DEFAULT 'Undefined')")
    cursor.execute("CREATE TABLE countries(country_id SERIAL PRIMARY KEY," +
                   "country_name VARCHAR(15))")
    cursor.execute("CREATE TABLE videos(video_id SERIAL PRIMARY KEY ," +
                   "video_name VARCHAR(100) DEFAULT 'Undefined'," +
                   "video_source VARCHAR(100) DEFAULT 'Undefined'," +
                   "genre_id INT)")
    cursor.execute("CREATE TABLE genres(genre_id SERIAL PRIMARY KEY ," +
                   "genre_name VARCHAR(15) DEFAULT 'Undefined')")


def yes_or_no(reply):
    if reply == "ДА":
        return True
    else:
        return False


def get_insert_information():
    first_name = 'Undefined'
    last_name = 'Undefined'
    birthday = 'Undefined'
    sex = 'Undefined'
    while True:
        video_source = input("Введите ссылку на видео:")
        if video_source == "":
            print("Вы должны ввести ссылку на видео!")
        else:
            break
    while True:
        video_name = input("Введите название видео:")
        if video_name == "":
            print("Вы должны ввести название видео!")
        else:
            break
    country_name = input("Введите страну создания(если не знаете оставьте пустым):")
    genre_name = input("Введите жанр видео(если не знаете оставьте пустым):")
    artist_name = input("Введите псевдоним автора(если не знаете оставьте пустым):")
    if artist_name != "":
        if yes_or_no(input('Хотите заполнить дополнительную информацию об авторе?[ДА/НЕТ]')):
            first_name = input("Введите имя автора(если не знаете оставьте пустым):")
            last_name = input("Введите фамилию автора(если не знаете оставьте пустым):")
            while True:
                birthday = input(
                    "Введите дату рождения автора в формате дд/мм/гггг(если не знаете оставьте пустым):")
                if re.fullmatch('\d\d/\d\d/\d{4}', birthday) or birthday == '':
                    break
                else:
                    print('Неверный формат даты, введите заново:')
            sex = input("Введите пол автора(если не знаете оставьте пустым):")
    call_insert(video_source, video_name, artist_name, country_name, genre_name, first_name, last_name, birthday, sex)


def call_insert(video_source, video_name, artist_name, country_name, genre_name, first_name, last_name, birthday, sex):
    if video_source == '':
        video_source = 'Undefined'
    if video_name == '':
        video_name = 'Undefined'
    if artist_name == '':
        artist_name = 'Undefined'
    if country_name == '':
        country_name = 'Undefined'
    if genre_name == '':
        genre_name = 'Undefined'
    if first_name == '':
        first_name = 'Undefined'
    if last_name == '':
        last_name = 'Undefined'
    if birthday == '':
        birthday = 'Undefined'
    if sex == '':
        sex = 'Undefined'
    insert_video(video_source, video_name, artist_name, country_name, genre_name, first_name, last_name, birthday, sex)


def insert_video(video_source, video_name, artist_name, country_name, genre_name, first_name, last_name, birthday, sex):
    cursor.execute("INSERT INTO genres (genre_name) VALUES ('" + genre_name + "') RETURNING genre_id")
    genre_id = str(cursor.fetchall()[0][0])
    cursor.execute("INSERT INTO countries (country_name) VALUES ('" + country_name + "') RETURNING country_id")
    country_id = str(cursor.fetchall()[0][0])
    cursor.execute("INSERT INTO videos (video_name,video_source,genre_id) VALUES ('"
                   + video_name + '\',\'' + video_source + '\',\'' + genre_id + "') RETURNING video_id")
    video_id = str(cursor.fetchall()[0][0])
    cursor.execute("INSERT INTO persons (nickname,last_name,first_name,birthday,sex) VALUES ('"
                   + artist_name + '\',\'' + last_name + '\',\'' + first_name + '\',\'' + birthday + '\',\'' +
                   sex + "') RETURNING artist_id")
    artist_id = str(cursor.fetchall()[0][0])
    cursor.execute("INSERT INTO artists (artist_id,country_id,video_id) VALUES ('"
                   + artist_id + '\',\'' + country_id + '\',\'' + video_id + "')")
    conn.commit()
    print("Видео успешно добавлено!")


def get_select_information():
    print("Выберите номер поля для поиска")
    field_dict = {'Ссылка на видео': '',
                  'Название видео': '',
                  'Псведоним создателя': '',
                  'Жанр видео': '',
                  'Страна создания': '',
                  'Имя создателя': '',
                  'Фамилия создателя': '',
                  'День рождения создателя': '',
                  'Пол создателя': ''}
    field_num = {'Ссылка на видео': '',
                 'Название видео': '',
                 'Псведоним создателя': '',
                 'Жанр видео': '',
                 'Страна создания': '',
                 'Имя создателя': '',
                 'Фамилия создателя': '',
                 'День рождения создателя': '',
                 'Пол создателя': ''}
    while True:
        i = 1
        for field in field_dict.keys():
            if field_dict[field] == '':
                field_num[field] = str(i)
                print(str(i) + '.' + field)
                i += 1
        while True:
            field_number = input("Введите номер поля:")
            if field_number.isdigit():
                if int(field_number) > i - 1 or int(field_number) < 1:
                    print('Некорректный номер поля, ввведите заново:')
                else:
                    break
            else:
                print('Некорректный номер поля, ввведите заново:')
        for field in field_num.keys():
            if field_num[field] == field_number:
                field_name = field
        field_dict[field_name] = input('Введите значение:')
        if not yes_or_no(input('Хотите указать дополнительную информацию[ДА/НЕТ]'
                               '')) or i == 1:
            break
    call_select(field_dict)


def call_select(field_dict):
    call_line = ''
    if field_dict['Ссылка на видео'] != '':
        call_line += "videos.video_source='" + field_dict['Ссылка на видео'] + "' AND "
    if field_dict['Название видео'] != '':
        call_line += "videos.video_name='" + field_dict['Название видео'] + "' AND "
    if field_dict['Псведоним создателя'] != '':
        call_line += "persons.nickname='" + field_dict['Псведоним создателя'] + "' AND "
    if field_dict['Страна создания'] != '':
        call_line += "countries.country_name='" + field_dict['Страна создания'] + "' AND "
    if field_dict['Жанр видео'] != '':
        call_line += "genres.genre_name='" + field_dict['Жанр видео'] + "' AND "
    if field_dict['Имя создателя'] != '':
        call_line += "persons.first_name='" + field_dict['Имя создателя'] + "' AND "
    if field_dict['Фамилия создателя'] != '':
        call_line += "persons.last_name='" + field_dict['Фамилия создателя'] + "' AND "
    if field_dict['День рождения создателя'] != '':
        call_line += "persons.birthday='" + field_dict['День рождения создателя'] + "' AND "
    if field_dict['Пол создателя'] != '':
        call_line += "persons.sex='" + field_dict['Пол создателя'] + "' AND "
    select_video(call_line[:-5])


def select_video(call_line):
    cursor.execute(
        "SELECT artists.artist_id,artists.country_id,artists.video_id," +
        "genres.genre_id,videos.video_name,videos.video_source FROM artists " +
        "JOIN persons ON artists.artist_id=persons.artist_id " +
        "JOIN countries ON artists.country_id=countries.country_id " +
        "JOIN videos ON artists.video_id=videos.video_id " +
        "JOIN genres ON genres.genre_id= videos.genre_id " +
        "WHERE " + call_line)
    result = cursor.fetchall()
    if len(result) == 0:
        print("Ничего не найдено")
    else:
        print("Найдено " + str(len(result)) + " результатов!")
        print("Что вы хотите сделать с найденными полями?Введите номер команды\n1.ПОКАЗАТЬ\n2.УДАЛИТЬ")
        while True:
            comm = input()
            if comm == '1':
                output(result)
                break
            elif comm == '2':
                delete_video(result)
                break
            else:
                print("Неизвестная команда,введите заново:")


def delete_video(out):
    for field in out:
        cursor.execute("DELETE FROM artists WHERE artist_id='" + str(field[0]) + "' AND " +
                       "country_id='" + str(field[1]) + "' AND " + "video_id='" + str(field[2]) + "'")
        cursor.execute("DELETE FROM persons WHERE artist_id='" + str(field[0]) + "'")
        cursor.execute("DELETE FROM countries WHERE country_id='" + str(field[1]) + "'")
        cursor.execute("DELETE FROM videos WHERE video_id='" + str(field[2]) + "'")
        cursor.execute("DELETE FROM genres WHERE genre_id='" + str(field[3]) + "'")
    conn.commit()
    print("Видео успешно удалено!")


def show_video():
    cursor.execute(
        "SELECT videos.video_name,videos.video_source FROM artists " +
        "JOIN persons ON artists.artist_id=persons.artist_id " +
        "JOIN countries ON artists.country_id=countries.country_id " +
        "JOIN videos ON artists.video_id=videos.video_id " +
        "JOIN genres ON genres.genre_id= videos.genre_id ")
    result = cursor.fetchall()
    if len(result) == 0:
        print("Нет записей")
    else:
        print("Найдено " + str(len(result)) + " результатов!")
        output(result)


def output(out):
    for field in out:
        print("Название видео:" + field[len(field) - 2] + "\t\t\tСсылка на видео:" + field[len(field) - 1])


remake_db()
create_db()

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
        get_insert_information()
    elif command == "ПОИСК":
        get_select_information()
    elif command == "ПОКАЗАТЬ":
        show_video()
    elif command == "ВЫХОД":
        break
    else:
        print("Неизвестная команда, повторите попытку:")
conn.close()
print("Соединение завершено")
