import sqlite3
from songs_funcs import sorting_hat


"""Creation of DB and a cursor"""
conn = sqlite3.connect('songs.db')
cur = conn.cursor()

# """Deleting a table"""
# cur.execute("DROP TABLE eli_songs")

"""Creation of columns in DB"""
# cur.execute("""CREATE TABLE eli_songs (
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

"""Function for sorting from the list """
# sorting_hat(songs, conn, cur)


# conn.commit()
#
# conn.close()
