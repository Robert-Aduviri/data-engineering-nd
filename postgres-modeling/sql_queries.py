# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

# The only difference between TEXT and VARCHAR(n) is that you can limit the maximum
# length of a VARCHAR column, for example, VARCHAR(255) does not allow inserting a
# string more than 255 characters long.

# The main reason for primary and foreign keys is to enforce data consistency.

songplay_table_create = """
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id VARCHAR,
    start_time TIMESTAMP,
    user_id INT,
    level VARCHAR(10),
    song_id VARCHAR,
    artist_id VARCHAR,
    session_id INT,
    location VARCHAR,
    user_agent VARCHAR
)
"""

user_table_create = """
CREATE TABLE IF NOT EXISTS users (
    user_id INT,
    first_name VARCHAR,
    last_name VARCHAR,
    gender VARCHAR(10),
    level VARCHAR(10)
)
"""

song_table_create = """
CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR,
    title VARCHAR,
    artist_id VARCHAR,
    year INT,
    duration DECIMAL
)
"""

artist_table_create = """
CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR,
    name VARCHAR,
    location VARCHAR,
    latitude VARCHAR,
    longitude VARCHAR
)
"""

# https://stackoverflow.com/questions/11799160/postgresql-field-type-for-unix-timestamp/22972434
# BIGINT is the best choice for storing a large unix timestamp,
# but it might be best to store the timestamp in the ISO 8601 standard format,
# represented in PostgreSQL as the TIMESTAMP data type

time_table_create = """
CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP,
    hour INT,
    day INT,
    week INT,
    month INT,
    year INT,
    weekday INT
)
"""

# INSERT RECORDS

songplay_table_insert = """
INSERT INTO songplays (
    songplay_id, start_time, user_id, level, song_id, artist_id,
    session_id, location, user_agent
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

user_table_insert = """
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
"""

song_table_insert = """
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
"""

artist_table_insert = """
INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
"""


time_table_insert = """
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

# FIND SONGS

song_select = """
SELECT songs.song_id, songs.artist_id
FROM songs
LEFT JOIN artists ON songs.artist_id = artists.artist_id
WHERE songs.title = %s
  AND artists.name = %s
  AND songs.duration = %s
"""

# QUERY LISTS

create_table_queries = [
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]
