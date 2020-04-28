import os
import glob
import psycopg2
import pandas as pd
import numpy as np

from sql_queries import *


def process_song_file(cur, filepath):
    # open song file
    df = pd.read_json(filepath, lines=True).set_index('num_songs')

    # insert song record
    song_data = df.loc[1, ['song_id', 'title', 'artist_id',
                           'year', 'duration']].to_numpy().tolist()

    # perform data type conversions
    song_data = list(map(convert_np_to_native, song_data))

    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = df.loc[1, ['artist_id', 'artist_name',
                             'artist_location', 'artist_latitude', 'artist_longitude']]

    artist_data = artist_data.fillna(0, inplace=True).to_numpy().tolist()
    # perform data type conversions
    artist_data = list(map(convert_np_to_native, artist_data))

    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df.loc[df['page'] == 'NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df.ts, unit='ms').drop_duplicates()
    
    # insert time data records
    time_data = (t.loc[:], t.dt.hour, t.dt.day, t.dt.week,
                 t.dt.month, t.dt.year, t.dt.weekday)
    column_labels = ('start_time', 'hour', 'day',
                     'week', 'month', 'year', 'weekday')
    # https://stackoverflow.com/questions/18837262/convert-python-dict-into-a-dataframe
    time_df = pd.DataFrame(dict(zip(column_labels, time_data)))

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df.loc[:, ['userId', 'firstName',
                         'lastName', 'gender', 'level']].drop_duplicates()

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get song_id and artist_id from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            song_id, artist_id = results
        else:
            song_id, artist_id = None, None

        # insert songplay record
        songplay_data = (str(pd.to_datetime(row.ts, unit='ms')), row.userId, row.level,
                         song_id, artist_id, row.sessionId, row.location, row.userAgent)

        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def convert_np_to_native(value):
    # convert numpy to native types to avoid problems during DB processing
    if isinstance(value, np.int32):
        return value.item()
    if isinstance(value, np.int64):
        return value.item()
    if isinstance(value, np.float64):
        return value.item()
    # default
    return value


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
