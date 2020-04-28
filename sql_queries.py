# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS f_songplays;"
user_table_drop = "DROP TABLE IF EXISTS d_users;"
song_table_drop = "DROP TABLE IF EXISTS d_songs;"
artist_table_drop = "DROP TABLE IF EXISTS d_artists;"
time_table_drop = "DROP TABLE IF EXISTS d_time;"

# CREATE TABLES

songplay_table_create = ("CREATE TABLE IF NOT EXISTS f_songplays \
  (songplay_id serial PRIMARY KEY, start_time timestamp, user_id int, \
  level varchar(10), song_id varchar(18), artist_id varchar(18), \
  session_id int, location varchar(200), user_agent varchar(200));")

user_table_create = ("CREATE TABLE IF NOT EXISTS d_users \
  (user_id int PRIMARY KEY, first_name varchar(80) NOT NULL, last_name varchar(100) NOT NULL, \
  gender character NOT NULL, level varchar(10) NOT NULL);")

song_table_create = ("CREATE TABLE IF NOT EXISTS d_songs \
  (song_id varchar(18) PRIMARY KEY, title varchar(200) NOT NULL, artist_id varchar(18) NOT NULL, \
  year int, duration numeric);")

artist_table_create = ("CREATE TABLE IF NOT EXISTS d_artists \
  (artist_id varchar(18) PRIMARY KEY, name varchar(200) NOT NULL, \
  location varchar(200), latitude numeric, longitude numeric);")

time_table_create = ("CREATE TABLE IF NOT EXISTS d_times \
  (start_time timestamp PRIMARY KEY, hour smallint, day smallint NOT NULL, \
  week smallint NOT NULL, month smallint NOT NULL, year smallint NOT NULL, weekday smallint NOT NULL);")

# INSERT RECORDS

# use DEFAULT value for songplay_id as it is a serial
songplay_table_insert = ("INSERT INTO f_songplays \
  (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) \
  VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

# what to do in case of conflict ? the user data should be TIME DEPENDENT
user_table_insert = ("INSERT INTO d_users \
  (user_id, first_name, last_name, gender, level) \
  VALUES(%s, %s, %s, %s, %s) \
  ON CONFLICT DO NOTHING")
# potentially no conflict to expect
song_table_insert = ("INSERT INTO d_songs \
  (song_id, title, artist_id, year, duration) \
  VALUES(%s, %s, %s, %s, %s) \
  ON CONFLICT DO NOTHING")
# potentially no conflict to expect
artist_table_insert = ("INSERT INTO d_artists \
  (artist_id, name, location, latitude, longitude) \
  VALUES(%s, %s, %s, %s, %s) \
  ON CONFLICT DO NOTHING")
# in case of conflict do nothing
time_table_insert = ("INSERT INTO d_times \
  (start_time, hour, day, week, month, year, weekday) \
  VALUES(%s, %s, %s, %s, %s, %s, %s) \
  ON CONFLICT DO NOTHING")

# FIND SONGS

song_select = ("SELECT song_id, d_artists.artist_id FROM ( \
    d_songs JOIN d_artists ON d_artists.artist_id=d_songs.artist_id ) \
    WHERE title=%s AND name=%s AND duration=%s;")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
