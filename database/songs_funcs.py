def sorting_hat(songs_list: list, db_connection, db_cursor) -> None:
    """
    Function for sorting songs from a song_list
    CHECK!!!
    a) names of button and number of buttons
    b) name of SQL_table
    """
    for i_song in songs_list:
        print('Песня:', i_song)
        next_step_check = True
        while next_step_check:
            choice = input(f'Enter the number:\n1 - Red button (bad)'
                           f'\n2- Yellow button (good)'
                           f'\n3 - Violet button(best)'
                           f'\n4 - Black button (skull)'
                           f'\n: ')

            insertion = """INSERT INTO eli_songs 
            (a_song, blue_button, red_button, green_button, orange_button, violet_button, pink_button, black_button)
             VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
            if choice == '1':
                button_tuple = (i_song, True, True, True, False, False, False, False)
            elif choice == '2':
                button_tuple = (i_song, True, False, True, True, False, False, False)
            elif choice == '3':
                button_tuple = (i_song, True, False, True, True, True, False, False)
            elif choice == '4':
                button_tuple = (i_song, True, False, False, False, False, False, True)

            else:
                print('Неверный ввод')

            db_cursor.execute(insertion, button_tuple)
            db_connection.commit()
            next_step_check = False

