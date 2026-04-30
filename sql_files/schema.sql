DROP DATABASE IF EXISTS steam_tracker;
CREATE DATABASE steam_tracker;
USE steam_tracker;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    join_date DATE DEFAULT (CURRENT_DATE)
);

CREATE TABLE games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    developer VARCHAR(100),
    release_year INT CHECK (release_year >= 1970),
    price DECIMAL(6,2) CHECK (price >= 0)
);

CREATE TABLE genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE game_genres (
    game_genre_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    genre_id INT NOT NULL,

    FOREIGN KEY (game_id) REFERENCES games(game_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE user_library (
    user_game_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    game_id INT NOT NULL,
    hours_played INT DEFAULT 0 CHECK (hours_played >= 0),
    status VARCHAR(20) DEFAULT 'wishlist',
    date_added DATE DEFAULT (CURRENT_DATE),

    FOREIGN KEY (user_id) REFERENCES users(user_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (game_id) REFERENCES games(game_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CHECK (status IN ('wishlist', 'owned', 'playing', 'completed'))
);

CREATE TABLE achievements (
    achievement_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,

    FOREIGN KEY (game_id) REFERENCES games(game_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);