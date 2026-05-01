import mysql.connector
from mysql.connector import Error


# ---------------- CONNECTION ----------------
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


# ---------------- USERS ----------------
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
        for row in results:
            print(row)

    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def delete_user(connection, user_id):
    try:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))

        connection.commit()
        print("User deleted")

    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


# ---------------- GAMES + GENRE ----------------
def add_game_with_genre(connection, title, developer, year, price, genre_name):
    try:
        cursor = connection.cursor()

        connection.start_transaction()

        # Insert game
        cursor.execute(
            """
            INSERT INTO games (title, developer, release_year, price)
            VALUES (%s, %s, %s, %s)
            """,
            (title, developer, year, price)
        )

        game_id = cursor.lastrowid

        # Ensure genre exists
        cursor.execute(
            "INSERT IGNORE INTO genres (genre_name) VALUES (%s)",
            (genre_name,)
        )

        # Get genre id
        cursor.execute(
            "SELECT genre_id FROM genres WHERE genre_name = %s",
            (genre_name,)
        )
        genre_id = cursor.fetchone()[0]

        # Link game + genre
        cursor.execute(
            """
            INSERT INTO game_genres (game_id, genre_id)
            VALUES (%s, %s)
            """,
            (game_id, genre_id)
        )

        connection.commit()
        print("Game and genre added")

    except Error as e:
        connection.rollback()
        print(f"Error: {e}")
    finally:
        cursor.close()


# ---------------- LIBRARY ----------------
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


# ---------------- UPDATE ----------------
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
        print("Playtime updated")

    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


# ---------------- VIEW WITH FILTERS ----------------
def view_libraries(connection, username=None, genre=None, min_hours=None):
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
        for row in results:
            print(row)

    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()