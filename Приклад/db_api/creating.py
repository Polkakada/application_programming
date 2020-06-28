def delete_db(cursor):
    cursor.execute("DROP TABLE artists")
    cursor.execute("DROP TABLE persons")
    cursor.execute("DROP TABLE countries")
    cursor.execute("DROP TABLE videos")
    cursor.execute("DROP TABLE genres")


def create_db(cursor):
    cursor.execute("CREATE TABLE artists(artist_id INT ," +
                   "country_id INT ," +
                   "video_id INT )")
    cursor.execute("CREATE TABLE persons(artist_id SERIAL PRIMARY KEY," +
                   "last_name VARCHAR(200) DEFAULT 'Undefined'," +
                   "nickname VARCHAR(200) DEFAULT 'Undefined'," +
                   "first_name VARCHAR(200) DEFAULT 'Undefined'," +
                   "birthday VARCHAR(10) DEFAULT 'Undefined'," +
                   "sex VARCHAR(10) DEFAULT 'Undefined')")
    cursor.execute("CREATE TABLE countries(country_id SERIAL PRIMARY KEY," +
                   "country_name VARCHAR(200))")
    cursor.execute("CREATE TABLE videos(video_id SERIAL PRIMARY KEY ," +
                   "video_name VARCHAR(500) DEFAULT 'Undefined'," +
                   "video_source VARCHAR(500) DEFAULT 'Undefined'," +
                   "genre_id INT)")
    cursor.execute("CREATE TABLE genres(genre_id SERIAL PRIMARY KEY ," +
                   "genre_name VARCHAR(50) DEFAULT 'Undefined')")

