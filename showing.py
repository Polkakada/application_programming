def show_video(cursor):
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
