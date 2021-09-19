import glob
import os
from typing import Callable

import pandas as pd
import psycopg2

import sql_queries


def process_song_file(cur, filepath: str) -> None:
    """
    Reads the song json file and inserts its data into the songs and artists tables
    in Postgres

    Arguments:
        cur: the cursor object
        filepath: log data file path
    """
    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    for song_record in df[
        [
            "song_id",
            "title",
            "artist_id",
            "year",
            "duration",
        ]
    ].values:
        cur.execute(sql_queries.song_table_insert, song_record)

    # insert artist record
    for artist_record in df[
        [
            "artist_id",
            "artist_name",
            "artist_location",
            "artist_latitude",
            "artist_longitude",
        ]
    ].values:
        cur.execute(sql_queries.artist_table_insert, artist_record)


def process_log_file(cur, filepath: str) -> None:
    """
    Reads the log json file and inserts its data into the time, users and
    songplays tables in Postgres

    Arguments:
        cur: the cursor object
        filepath: log data file path
    """
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df.page == "NextSong"].copy()

    # convert timestamp column to datetime
    df["ts"] = pd.to_datetime(df["ts"], unit="ms")

    # insert time data records
    column_labels = ["hour", "day", "week", "month", "year", "weekday"]

    for column_label in column_labels:
        if column_label == "week":
            # FutureWarning: Series.dt.weekofyear and Series.dt.week have been
            # deprecated.  Please use Series.dt.isocalendar().week instead.
            df[column_label] = df["ts"].dt.isocalendar().week
        else:
            df[column_label] = getattr(df["ts"].dt, column_label)

    time_df = pd.DataFrame()
    time_df["start_time"] = df["ts"]
    time_df = pd.concat([time_df, df[column_labels]], axis=1)
    time_df.head()

    for i, row in time_df.iterrows():
        cur.execute(sql_queries.time_table_insert, list(row))

    # load user table
    user_df = df[["userId", "firstName", "lastName", "gender", "level"]]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(sql_queries.user_table_insert, row)

    # insert songplay records
    for _, row in df.iterrows():

        # get songid and artistid from song and artist tables
        cur.execute(sql_queries.song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (
            row.ts,
            row.userId,
            row.level,
            songid,
            artistid,
            row.sessionId,
            row.location,
            row.userAgent,
        )
        cur.execute(sql_queries.songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath: str, func: Callable) -> None:
    """
    Processes all the json files located in the specified `filepath` by applying
    the injected processing function `func` to each file, inserting the data into
    the Postgres database, using the provided DB connection `conn` and cursor `cur`

    Arguments:
        cur: the cursor object
        conn: connection to the database
        filepath: log data or song data file path
        func: function that transforms the data and inserts it into the database
    """
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, "*.json"))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print("{} files found in {}".format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print("{}/{} files processed.".format(i, num_files))


def main():
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=student password=student"
    )
    cur = conn.cursor()

    process_data(cur, conn, filepath="data/song_data", func=process_song_file)
    process_data(cur, conn, filepath="data/log_data", func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
