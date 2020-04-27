# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS f_songplays;"
user_table_drop = "DROP TABLE IF EXISTS d_users;"
song_table_drop = "DROP TABLE IF EXISTS d_songs;"
artist_table_drop = "DROP TABLE IF EXISTS d_artists;"
time_table_drop = "DROP TABLE IF EXISTS d_time;"

# CREATE TABLES

songplay_table_create = ("CREATE TABLE IF NOT EXISTS f_songplays \
  (songplay_id int, start_time timestamp, user_id int, \
  level varchar(10), song_id int, artist_id int, \
  session_id int, location varchar(200), user_agent varchar(200));")

user_table_create = ("CREATE TABLE IF NOT EXISTS d_users \
  (user_id int, first_name varchar(80), last_name varchar(100), gender character, level varchar(10));")

song_table_create = ("CREATE TABLE IF NOT EXISTS d_songs \
  (song_id int, title varchar(200), artist_id int, year smallint, duration smallint);")

artist_table_create = ("CREATE TABLE IF NOT EXISTS d_artists \
  (artist_id int, name varchar(200), location varchar(200), latitude int, longitude int);")

time_table_create = ("CREATE TABLE IF NOT EXISTS d_times \
  (start_time timestamp, hour smallint, day smallint, week smallint, month smallint, year smallint, weekday smallint);")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
