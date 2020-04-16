

def delete_video(out,cursor):
    for field in out:
        cursor.execute("DELETE FROM artists WHERE artist_id='" + str(field[0]) + "' AND " +
                       "country_id='" + str(field[1]) + "' AND " + "video_id='" + str(field[2]) + "'")
        cursor.execute("DELETE FROM persons WHERE artist_id='" + str(field[0]) + "'")
        cursor.execute("DELETE FROM countries WHERE country_id='" + str(field[1]) + "'")
        cursor.execute("DELETE FROM videos WHERE video_id='" + str(field[2]) + "'")
        cursor.execute("DELETE FROM genres WHERE genre_id='" + str(field[3]) + "'")

    print("Видео успешно удалено!")
