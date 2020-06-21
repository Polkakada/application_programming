def show_video(cursor):
    cursor.execute(
        "SELECT persons.nickname,videos.video_name,videos.video_source," +
        "countries.country_name,genres.genre_name,artists.artist_id," +
        "countries.country_id,videos.video_id,genres.genre_id " +
        "FROM artists JOIN persons ON artists.artist_id=persons.artist_id " +
        "JOIN countries ON artists.country_id=countries.country_id " +
        "JOIN videos ON artists.video_id=videos.video_id " +
        "JOIN genres ON genres.genre_id= videos.genre_id ")
    result = cursor.fetchall()
    if len(result) == 0:
        return "Нет записей"
    else:
        return output(result)


def output(out):
    s = []
    for field in out:
        s.append("Название видео: " + field[1] +
                 "\tСсылка на видео: " + field[2] +
                 "\tАвтор: " + field[0] +
                 "\tЖанр: " + field[4] +
                 "\tСтрана: " + field[3])
    return s
