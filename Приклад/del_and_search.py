import showing


def call_find(field_dict, cursor, mod=1):
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
    if field_dict['День рождения создателя'] != '01.01.1753':
        call_line += "persons.birthday='" + field_dict['День рождения создателя'] + "' AND "
    if field_dict['Пол создателя'] != '':
        call_line += "persons.sex='" + field_dict['Пол создателя'] + "' AND "
    call_line = call_line[:-5]
    return select_video(call_line, cursor, mod)


def select_video(call_line, cursor, mod):
    cursor.execute(
        "SELECT persons.nickname,videos.video_name,videos.video_source," +
        "countries.country_name,genres.genre_name,artists.artist_id," +
        "countries.country_id,videos.video_id,genres.genre_id " +
        "FROM artists JOIN persons ON artists.artist_id=persons.artist_id " +
        "JOIN countries ON artists.country_id=countries.country_id " +
        "JOIN videos ON artists.video_id=videos.video_id " +
        "JOIN genres ON genres.genre_id= videos.genre_id " +
        "WHERE " + call_line)
    result = cursor.fetchall()

    if mod == 1:
        delete_video(result, cursor)

        return ""
    elif mod == 2:

        if len(result) == 0:

            return "Нет записей"
        else:

            return showing.output(result)
    else:
        if len(result) == 0:
            return True
        else:
            return False


def delete_video(out, cursor):
    for field in out:
        cursor.execute("DELETE FROM artists WHERE artist_id='" + str(field[5]) + "' AND " +
                       "country_id='" + str(field[6]) + "' AND " + "video_id='" + str(field[2]) + "'")
        cursor.execute("DELETE FROM persons WHERE artist_id='" + str(field[5]) + "'")
        cursor.execute("DELETE FROM countries WHERE country_id='" + str(field[6]) + "'")
        cursor.execute("DELETE FROM videos WHERE video_id='" + str(field[7]) + "'")
        cursor.execute("DELETE FROM genres WHERE genre_id='" + str(field[8]) + "'")

    print("Видео успешно удалено!")


def fullOut(out):
    field_dict = {'Ссылка на видео': out[0][5],
                  'Название видео': out[0][4],
                  'Псведоним создателя': out[0][2],
                  'Жанр видео': out[0][8],
                  'Страна создания': out[0][7],
                  'Имя создателя': out[0][1],
                  'Фамилия создателя': out[0][0],
                  'День рождения создателя': out[0][3],
                  'Пол создателя': out[0][6]}
    return field_dict


def findFullInfo(source, name, author, genre, country, cursor):
    cursor.execute(
        "SELECT persons.last_name,persons.first_name,persons.nickname," +
        "persons.birthday,videos.video_name,videos.video_source,persons.sex," +
        "countries.country_name,genres.genre_name FROM artists " +
        "JOIN persons ON artists.artist_id=persons.artist_id " +
        "JOIN countries ON artists.country_id=countries.country_id " +
        "JOIN videos ON artists.video_id=videos.video_id " +
        "JOIN genres ON genres.genre_id= videos.genre_id " +
        "WHERE " + "videos.video_source='" + source + "' AND " + "videos.video_name='" + name +"' AND "+
        "persons.nickname='" + author + "' AND " + "genres.genre_name='" + genre +
        "' AND " + "countries.country_name='" + country + "'")
    result = cursor.fetchall()
    return fullOut(result)
