def call_insert(field_dict, cursor):
    if field_dict['Ссылка на видео'] == '':
        field_dict['Ссылка на видео'] = 'Undefined'
    if field_dict['Название видео'] == '':
        field_dict['Название видео'] = 'Undefined'
    if field_dict['Псведоним создателя'] == '':
        field_dict['Псведоним создателя'] = 'Undefined'
    if field_dict['Страна создания'] == '':
        field_dict['Страна создания'] = 'Undefined'
    if field_dict['Жанр видео'] == '':
        field_dict['Жанр видео'] = 'Undefined'
    if field_dict['Имя создателя'] == '':
        field_dict['Имя создателя'] = 'Undefined'
    if field_dict['Фамилия создателя'] == '':
        field_dict['Фамилия создателя'] = 'Undefined'
    if field_dict['День рождения создателя'] == '01.01.2200' or field_dict['День рождения создателя'] == "":
        field_dict['День рождения создателя'] = 'Undefined'
    if field_dict['Пол создателя'] == '':
        field_dict['Пол создателя'] = 'Undefined'
    insert_video(field_dict, cursor)


def insert_video(field_dict, cursor):
    cursor.execute("SELECT genres.genre_id From genres WHERE genres.genre_name='" + field_dict['Жанр видео'] + "'")
    genre_id = cursor.fetchall()
    if len(genre_id) == 0:
        cursor.execute("INSERT INTO genres (genre_name) VALUES ('" + field_dict['Жанр видео'] + "') RETURNING genre_id")
        genre_id = str(cursor.fetchall()[0][0])
    else:
        genre_id = str(genre_id[0][0])
    cursor.execute(
        "SELECT countries.country_id FROM countries WHERE countries.country_name='" + field_dict[
            'Страна создания'] + "'")
    country_id = cursor.fetchall()
    if len(country_id) == 0:
        cursor.execute("INSERT INTO countries (country_name) VALUES ('"
                       + field_dict['Страна создания'] + "') RETURNING country_id")
        country_id = str(cursor.fetchall()[0][0])
    else:
        country_id = str(country_id[0][0])
    cursor.execute(
        "SELECT videos.video_id FROM videos WHERE videos.video_name='" + field_dict['Название видео'] + "' AND " +
        "videos.video_source='" + field_dict['Ссылка на видео'] + "' AND " +
        "videos.genre_id='" + genre_id + "'")
    video_id = cursor.fetchall()
    if len(video_id) == 0:
        cursor.execute("INSERT INTO videos (video_name,video_source,genre_id) VALUES ('"
                       + field_dict['Название видео'] + '\',\''
                       + field_dict['Ссылка на видео'] + '\',\'' + genre_id + "') RETURNING video_id")
        video_id = str(cursor.fetchall()[0][0])
    else:
        video_id = str(video_id[0][0])
    cursor.execute("SELECT persons.artist_id FROM persons WHERE " +
                   "persons.nickname='" + field_dict['Псведоним создателя'] + "' AND " +
                   "persons.last_name='" + field_dict['Фамилия создателя'] + "' AND " +
                   "persons.first_name='" + field_dict['Имя создателя'] + "' AND " +
                   "persons.sex='" + field_dict['Пол создателя'] + "' AND " +
                   "persons.birthday='" + field_dict['День рождения создателя'] + "'")
    artist_id = cursor.fetchall()
    if len(artist_id) == 0:
        cursor.execute("INSERT INTO persons (nickname,last_name,first_name,birthday,sex) VALUES ('"
                       + field_dict['Псведоним создателя'] + '\',\''
                       + field_dict['Фамилия создателя'] + '\',\''
                       + field_dict['Имя создателя'] + '\',\''
                       + field_dict['День рождения создателя'] + '\',\''
                       + field_dict['Пол создателя'] + "') RETURNING artist_id")
        artist_id = str(cursor.fetchall()[0][0])
    else:
        artist_id = str(artist_id[0][0])
    cursor.execute("INSERT INTO artists (artist_id,country_id,video_id) VALUES ('"
                   + artist_id + '\',\'' + country_id + '\',\'' + video_id + "')")

    print("Видео успешно добавлено!")
