import sqlite3
from songs_db_funcs import sorting_hat


"""Creation of DB and a cursor"""
conn = sqlite3.connect('songs.db')
cur = conn.cursor()

# """Deleting a table"""
# cur.execute("DROP TABLE eli_songs")

"""Creation of columns in DB"""
# cur.execute("""CREATE TABLE ramm_songs (
# id integer PRIMARY KEY,
# a_song TEXT,
# blue_button BOOLEAN NOT NULL CHECK (blue_button IN (0, 1)),
# red_button BOOLEAN NOT NULL CHECK (red_button IN (0, 1)),
# green_button BOOLEAN NOT NULL CHECK (green_button IN (0, 1)),
# orange_button BOOLEAN NOT NULL CHECK (orange_button IN (0, 1)),
# violet_button BOOLEAN NOT NULL CHECK (violet_button IN (0, 1)),
# pink_button BOOLEAN NOT NULL CHECK (pink_button IN (0, 1)),
# black_button BOOLEAN NOT NULL CHECK (black_button IN (0, 1))
#
# )""")


# conn.commit()
#
# conn.close()

"""The list of songs for adding to DataBase"""
songs = ['Каверы - Один раз в год сады цветут...']


"""
Function for sorting from the list 
CHECK FILE "songs_db_funcs.py" BEFORE USING THE FUNCTION 
"""
# sorting_hat(songs, conn, cur)

# random_sel = "SELECT a_song FROM ramm_songs WHERE (?)=1 ORDER BY RANDOM() LIMIT 1"
# random_conditions = ('red_button', )
# random_execution = cur.execute(random_sel, random_conditions)
# print(random_execution.fetchall())

# conn.commit()
#
# conn.close()
