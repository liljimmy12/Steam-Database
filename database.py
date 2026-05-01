import mysql.connector
from mysql.connector import Error


# CONNECTION
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="steam_tracker"
        )
        return connection
    except Error as e:
        print(f"Connection error: {e}")
        return None


# -USERS
def add_user(connection, username, email):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO users (username, email) VALUES (%s, %s)"
        cursor.execute(query, (username, email))
        connection.commit()
        print("User added")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def view_users(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT user_id, username, email FROM users")
        results = cursor.fetchall()

        print("\nUsers:")
        print("-" * 40)
        for row in results:
            print(f"ID: {row[0]} | Username: {row[1]} | Email: {row[2]}")

    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


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
    finally:
        cursor.close()


# GAMES
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
        print(f"❌ Error: {e}")
    finally:
        cursor.close()


# GENRES
def add_genre(connection, genre_name):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT IGNORE INTO genres (genre_name) VALUES (%s)", (genre_name,))
        connection.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def add_game_genre(connection, game_id, genre_name):
    try:
        cursor = connection.cursor()

        add_genre(connection, genre_name)

        cursor.execute(
            "SELECT genre_id FROM genres WHERE genre_name = %s",
            (genre_name,)
        )
        genre_id = cursor.fetchone()[0]

        cursor.execute(
            "INSERT INTO game_genres (game_id, genre_id) VALUES (%s, %s)",
            (game_id, genre_id)
        )

        connection.commit()
        print("Genre added to game")

    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


# LIBRARY
def add_to_library_and_set_status(connection, user_id, game_id, status):
    try:
        cursor = connection.cursor()

        connection.start_transaction()

        cursor.execute(
            """
            INSERT INTO user_library (user_id, game_id, status, hours_played)
            VALUES (%s, %s, %s, 0)
            ON DUPLICATE KEY UPDATE status = VALUES(status)
            """,
            (user_id, game_id, status)
        )

        connection.commit()
        print("Library updated")

    except Error as e:
        connection.rollback()
        print(f"Error: {e}")
    finally:
        cursor.close()


def update_playtime(connection, user_id, game_id, hours):
    try:
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE user_library
            SET hours_played = %s
            WHERE user_id = %s AND game_id = %s
            """,
            (hours, user_id, game_id)
        )

        connection.commit()
        print("⏱Playtime updated")

    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def view_all_libraries(connection, username=None, genre=None, min_hours=None):
    try:
        cursor = connection.cursor()

        query = """
        SELECT users.username, games.title, user_library.hours_played, user_library.status
        FROM user_library
        JOIN users ON user_library.user_id = users.user_id
        JOIN games ON user_library.game_id = games.game_id
        """

        conditions = []
        values = []

        if genre:
            query += """
            JOIN game_genres ON games.game_id = game_genres.game_id
            JOIN genres ON game_genres.genre_id = genres.genre_id
            """
            conditions.append("genres.genre_name = %s")
            values.append(genre)

        if username:
            conditions.append("users.username = %s")
            values.append(username)

        if min_hours is not None:
            conditions.append("user_library.hours_played >= %s")
            values.append(min_hours)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        cursor.execute(query, values)
        results = cursor.fetchall()

        print("\nUser Libraries:")
        print("-" * 50)
        for row in results:
            print(f"{row[0]} | {row[1]} | {row[2]} hrs | {row[3]}")

    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()