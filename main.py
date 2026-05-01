from database import *


def main():
    connection = create_connection()
    if not connection:
        return

    while True:
        print("\nSteam Tracker")
        print("=" * 30)
        print("1. Add User")
        print("2. Add Game")
        print("3. Delete User + Library")
        print("4. Add Game to Library + Set Status")
        print("5. View All Libraries (Filter)")
        print("6. Update Playtime")
        print("7. Add Genre to Game")
        print("8. Exit")

        choice = input("\nChoose: ")

        try:
            # ADD USER
            if choice == "1":
                username = input("Username: ")
                email = input("Email: ")
                add_user(connection, username, email)

            # ADD GAME
            elif choice == "2":
                title = input("Title: ")
                developer = input("Developer: ")
                year = int(input("Release Year: "))
                price = float(input("Price: "))
                add_game(connection, title, developer, year, price)

            # DELETE USER
            elif choice == "3":
                view_users(connection)

                user_id = int(input("\nEnter User ID to delete: "))
                confirm = input("Are you sure? (y/n): ")

                if confirm.lower() == 'y':
                    delete_user_with_library(connection, user_id)

            # LIBRARY TRANSACTION
            elif choice == "4":
                user_id = int(input("User ID: "))
                game_id = int(input("Game ID: "))
                status = input("Status (wishlist, owned, playing, completed): ")

                add_to_library_and_set_status(
                    connection, user_id, game_id, status
                )

            # VIEW LIBRARIES
            elif choice == "5":
                print("\n--- Filters (press enter to skip) ---")

                username = input("Username: ").strip() or None
                genre = input("Genre: ").strip() or None
                min_hours_input = input("Min hours: ").strip()

                min_hours = int(min_hours_input) if min_hours_input else None

                view_all_libraries(connection, username, genre, min_hours)

            # UPDATE PLAYTIME
            elif choice == "6":
                user_id = int(input("User ID: "))
                game_id = int(input("Game ID: "))
                hours = int(input("New hours played: "))
                update_playtime(connection, user_id, game_id, hours)

            # ADD GENRE
            elif choice == "7":
                game_id = int(input("Game ID: "))
                genre = input("Genre: ")
                add_game_genre(connection, game_id, genre)

            # EXIT
            elif choice == "8":
                break

            else:
                print("Invalid choice")

        except ValueError:
            print("Invalid input type")

    connection.close()


if __name__ == "__main__":
    main()