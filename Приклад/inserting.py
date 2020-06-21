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
    if field_dict['День рождения создателя'] == '01.01.1753':
        field_dict['День рождения создателя'] = 'Undefined'
    if field_dict['Пол создателя'] == '':
        field_dict['Пол создателя'] = 'Undefined'
    print("ok")
    insert_video(field_dict, cursor)


def insert_video(field_dict, cursor):
    cursor.execute("INSERT INTO genres (genre_name) VALUES ('" + field_dict['Жанр видео'] + "') RETURNING genre_id")
    genre_id = str(cursor.fetchall()[0][0])
    cursor.execute("INSERT INTO countries (country_name) VALUES ('"
                   + field_dict['Страна создания'] + "') RETURNING country_id")
    country_id = str(cursor.fetchall()[0][0])
    cursor.execute("INSERT INTO videos (video_name,video_source,genre_id) VALUES ('"
                   + field_dict['Название видео'] + '\',\''
                   + field_dict['Ссылка на видео'] + '\',\'' + genre_id + "') RETURNING video_id")
    video_id = str(cursor.fetchall()[0][0])
    cursor.execute("INSERT INTO persons (nickname,last_name,first_name,birthday,sex) VALUES ('"
                   + field_dict['Псведоним создателя'] + '\',\''
                   + field_dict['Фамилия создателя'] + '\',\''
                   + field_dict['Имя создателя'] + '\',\''
                   + field_dict['День рождения создателя'] + '\',\''
                   + field_dict['Пол создателя'] + "') RETURNING artist_id")
    artist_id = str(cursor.fetchall()[0][0])
    cursor.execute("INSERT INTO artists (artist_id,country_id,video_id) VALUES ('"
                   + artist_id + '\',\'' + country_id + '\',\'' + video_id + "')")

    print("Видео успешно добавлено!")
