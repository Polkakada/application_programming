import deletion


def get_select_information(cursor):
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
    call_select(field_dict, cursor)


def call_select(field_dict, cursor):
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
    select_video(call_line[:-5], cursor)


def select_video(call_line, cursor):
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
                deletion.delete_video(result, cursor)
                break
            else:
                print("Неизвестная команда,введите заново:")


def output(out):
    for field in out:
        print("Название видео:" + field[len(field) - 2] + "\t\t\tСсылка на видео:" + field[len(field) - 1])


def yes_or_no(reply):
    if reply == "ДА":
        return True
    else:
        return False
