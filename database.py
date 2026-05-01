import mysql.connector
from mysql.connector import Error


# CONNECTION 
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",   # CHANGE THIS
            database="steam_tracker"
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


# USERS 
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


def delete_user_with_library(connection, user_id):
    try:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM user_library WHERE user_id = %s", (user_id,))
        cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))

        connection.commit()
        print("User and library deleted")
    except Error as e:
        print(f"Error: {e}")
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
        print(f"Error: {e}")
    finally:
        cursor.close()


# GENRES 
def add_genre(connection, genre_name):
    try:
        cursor = connection.cursor()
        query = "INSERT IGNORE INTO genres (name) VALUES (%s)"
        cursor.execute(query, (genre_name,))
        connection.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def add_game_genre(connection, game_id, genre_name):
    try:
        cursor = connection.cursor()

        # Ensure genre exists
        add_genre(connection, genre_name)

        # Get genre_id
        cursor.execute("SELECT genre_id FROM genres WHERE name = %s", (genre_name,))
        genre_id = cursor.fetchone()[0]

        # Link game + genre
        query = """
        INSERT INTO game_genres (game_id, genre_id)
        VALUES (%s, %s)
        """
        cursor.execute(query, (game_id, genre_id))
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

        query = """
        INSERT INTO user_library (user_id, game_id, status, hours_played)
        VALUES (%s, %s, %s, 0)
        ON DUPLICATE KEY UPDATE status = VALUES(status)
        """

        cursor.execute(query, (user_id, game_id, status))
        connection.commit()

        print("Library updated")

    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


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

        print("Playtime updated")

    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


# VIEW (FILTERED)
def view_all_libraries(connection, username=None, genre=None, min_hours=None):
    try:
        cursor = connection.cursor()

        query = """
        SELECT users.username, games.title, user_library.hours_played
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
            conditions.append("genres.name = %s")
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
            print(f"User: {row[0]} | Game: {row[1]} | Hours: {row[2]}")

    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()