from database import *


def main():
    connection = create_connection()
    if not connection:
        return

    while True:
        print("\nSteam Tracker")
        print("1. Add User")
        print("2. Add Game + Genre")
        print("3. Delete User")
        print("4. Add Game to Library + Set Status (Transaction)")
        print("5. View Libraries (Filters)")
        print("6. Update Playtime")
        print("7. View Users")
        print("8. Exit")

        choice = input("Choose: ")

        try:
            # ---------------- USER ----------------
            if choice == "1":
                username = input("Username: ")
                email = input("Email: ")
                add_user(connection, username, email)

            # ---------------- GAME + GENRE ----------------
            elif choice == "2":
                title = input("Title: ")
                developer = input("Developer: ")
                year = int(input("Release Year: "))
                price = float(input("Price: "))
                genre = input("Genre: ")

                add_game_with_genre(connection, title, developer, year, price, genre)

            # ---------------- DELETE USER ----------------
            elif choice == "3":
                view_users(connection)

                user_id = int(input("User ID to delete: "))
                confirm = input("Confirm delete (y/n): ")

                if confirm.lower() == "y":
                    delete_user(connection, user_id)

            # ---------------- TRANSACTION ----------------
            elif choice == "4":
                user_id = int(input("User ID: "))
                game_id = int(input("Game ID: "))
                status = input("Status (wishlist, owned, playing, completed): ")

                add_to_library_and_set_status(connection, user_id, game_id, status)

            # ---------------- VIEW FILTERED ----------------
            elif choice == "5":
                username = input("Username (blank for all): ").strip() or None
                genre = input("Genre (blank for all): ").strip() or None
                hours = input("Min hours (blank for all): ").strip()

                min_hours = int(hours) if hours else None

                view_libraries(connection, username, genre, min_hours)

            # ---------------- UPDATE ----------------
            elif choice == "6":
                user_id = int(input("User ID: "))
                game_id = int(input("Game ID: "))
                hours = int(input("Hours played: "))

                update_playtime(connection, user_id, game_id, hours)

            # ---------------- VIEW USERS ----------------
            elif choice == "7":
                view_users(connection)

            # ---------------- EXIT ----------------
            elif choice == "8":
                break

            else:
                print("Invalid choice")

        except ValueError:
            print("Invalid input")

    connection.close()


if __name__ == "__main__":
    main()