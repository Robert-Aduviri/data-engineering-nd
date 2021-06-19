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
    start_time INT,
    user_id VARCHAR,
    level VARCHAR(20),
    song_id VARCHAR,
    artist_id VARCHAR,
    session_id INT,
    location VARCHAR,
    user_agent VARCHAR
)
"""

user_table_create = """
CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR,
    first_name VARCHAR,
    last_name VARCHAR,
    gender VARCHAR,
    level VARCHAR
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

time_table_create = """
CREATE TABLE IF NOT EXISTS time (
    start_time INT,
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
"""

user_table_insert = """
"""

song_table_insert = """
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
"""

artist_table_insert = """
"""


time_table_insert = """
"""

# FIND SONGS

song_select = """
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
