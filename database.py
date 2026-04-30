import mysql.connector
from mysql.connector import Error

# Connecting the database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database='steam_tracker'
        )
        return connection
    except Error as e:
        print(f"Connection error: {e}")
        return None


# Create
def add_user(connection, username, email):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO users (username, email) VALUES (%s, %s)"
        cursor.execute(query, (username, email))
        connection.commit()
        print("User added")
    except Error as e:
        print(f"Error: {e}")


def add_game(connection, title, developer, year, price):
    try:
        cursor = connection.cursor()
        query = """
        INSERT INTO games (title, developer, release_year, price)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (title, developer, year, price))
        connection.commit()
        print("Game added")
    except Error as e:
        print(f"Error: {e}")


# Delete user + their library
def delete_user_with_library(connection, user_id):
    try:
        cursor = connection.cursor()
        connection.start_transaction()

        cursor.execute("DELETE FROM user_library WHERE user_id = %s", (user_id,))
        cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))

        connection.commit()
        print("User and library deleted")

    except Error as e:
        connection.rollback()
        print(f"Transaction failed: {e}")


# Add game to library + update status
def add_to_library_and_set_status(connection, user_id, game_id, status):
    try:
        cursor = connection.cursor()
        connection.start_transaction()

        # Add to library
        cursor.execute(
            "INSERT INTO user_library (user_id, game_id) VALUES (%s, %s)",
            (user_id, game_id)
        )

        # Update status
        cursor.execute(
            "UPDATE user_library SET status = %s WHERE user_id = %s AND game_id = %s",
            (status, user_id, game_id)
        )

        connection.commit()
        print("Game added to library and status set")

    except Error as e:
        connection.rollback()
        print(f"Transaction failed: {e}")


# Reading all libraries
def view_all_libraries(connection):
    try:
        cursor = connection.cursor()
        query = """
        SELECT users.username, games.title, user_library.hours_played
        FROM user_library
        JOIN users ON user_library.user_id = users.user_id
        JOIN games ON user_library.game_id = games.game_id
        """
        cursor.execute(query)
        results = cursor.fetchall()

        print("\nAll User Libraries:")
        for row in results:
            print(f"User: {row[0]} | Game: {row[1]} | Hours: {row[2]}")

    except Error as e:
        print(f"Error: {e}")


# Updating playtime
def update_playtime(connection, user_id, game_id, hours):
    try:
        cursor = connection.cursor()
        query = """
        UPDATE user_library
        SET hours_played = %s
        WHERE user_id = %s AND game_id = %s
        """
        cursor.execute(query, (hours, user_id, game_id))
        connection.commit()
        print("⏱Playtime updated")

    except Error as e:
        print(f"Error: {e}")