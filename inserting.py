import re


def yes_or_no(reply):
    if reply == "ДА":
        return True
    else:
        return False


def get_insert_information(cursor):
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
    call_insert(video_source, video_name, artist_name, country_name, genre_name, first_name, last_name, birthday, sex,
                cursor)


def call_insert(video_source, video_name, artist_name, country_name, genre_name, first_name, last_name, birthday, sex,
                cursor):
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
    insert_video(video_source, video_name, artist_name, country_name, genre_name, first_name, last_name, birthday, sex,
                 cursor)


def insert_video(video_source, video_name, artist_name, country_name, genre_name, first_name, last_name, birthday, sex,
                 cursor):
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

    print("Видео успешно добавлено!")


