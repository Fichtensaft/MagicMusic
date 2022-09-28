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
                           f'\n4 - Pink button (Lindemann)'
                           f'\n5 - Just blue (bad lindemann)'
                           f'\n6 - Black button (scythe)'
                           f'\n: ')

            insertion = """INSERT INTO eli_songs 
            (a_song, blue_button, red_button, green_button, orange_button, violet_button, pink_button, black_button)
             VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
            if choice == '1':
                button_tuple = (i_song, True, True, True, False, False, False, False)
                print(f"{i_song} has been added to Red button (bad)\n\n")
            elif choice == '2':
                button_tuple = (i_song, True, False, True, True, False, False, False)
                print(f"{i_song} has been added to Yellow button (good)\n\n")
            elif choice == '3':
                button_tuple = (i_song, True, False, True, True, True, False, False)
                print(f"{i_song} has been added to Violet button(best)\n\n")
            elif choice == '4':
                button_tuple = (i_song, True, False, False, False, False, True, False)
                print(f"{i_song} has been added to ink button (Lindemann)\n\n")
            elif choice == '5':
                button_tuple = (i_song, True, False, False, False, False, False, False)
                print(f"{i_song} has been added to Just blue (bad lindemann)\n\n")
            elif choice == '6':
                button_tuple = (i_song, True, False, False, False, False, False, True)
                print(f"{i_song} has been added to Skull")

            else:
                print('Неверный ввод')

            db_cursor.execute(insertion, button_tuple)
            db_connection.commit()
            next_step_check = False
