from database import *

def main():
    connection = create_connection()
    if not connection:
        return

    while True:
        print("\n🎮 Steam Tracker")
        print("1. Add User")
        print("2. Add Game")
        print("3. Delete User + Library")
        print("4. Add Game to Library + Set Status")
        print("5. View All User Libraries")
        print("6. Update Playtime")
        print("7. Exit")

        choice = input("Choose: ")

        try:
            if choice == "1":
                username = input("Username: ")
                email = input("Email: ")
                add_user(connection, username, email)

            elif choice == "2":
                title = input("Title: ")
                developer = input("Developer: ")
                year = int(input("Release Year: "))
                price = float(input("Price: "))
                add_game(connection, title, developer, year, price)

            elif choice == "3":
                user_id = int(input("User ID to delete: "))
                confirm = input("Are you sure? (y/n): ")
                if confirm.lower() == 'y':
                    delete_user_with_library(connection, user_id)

            elif choice == "4":
                user_id = int(input("User ID: "))
                game_id = int(input("Game ID: "))
                status = input("Status (wishlist, owned, playing, completed): ")
                add_to_library_and_set_status(connection, user_id, game_id, status)

            elif choice == "5":
                view_all_libraries(connection)

            elif choice == "6":
                user_id = int(input("User ID: "))
                game_id = int(input("Game ID: "))
                hours = int(input("New hours played: "))
                update_playtime(connection, user_id, game_id, hours)

            elif choice == "7":
                break

            else:
                print("❌ Invalid choice")

        except ValueError:
            print("❌ Invalid input type")

    connection.close()


if __name__ == "__main__":
    main()