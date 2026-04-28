-- johndoe's library
SELECT users.username, games.title, user_library.hours_played, user_library.status
FROM user_library
JOIN users ON user_library.user_id = users.user_id
JOIN games ON user_library.game_id = games.game_id
WHERE users.user_id = 1;

-- Total hours per user
SELECT users.username, SUM(user_library.hours_played) AS total_hours
FROM user_library
JOIN users ON user_library.user_id = users.user_id
GROUP BY users.username;

-- RPG games
SELECT games.title, genres.genre_name
FROM games
JOIN game_genres ON games.game_id = game_genres.game_id
JOIN genres ON game_genres.genre_id = genres.genre_id
WHERE genres.genre_name = 'RPG';

-- Eldenring achievements 
SELECT games.title, achievements.name, achievements.description
FROM achievements
JOIN games ON achievements.game_id = games.game_id
WHERE games.game_id = 1;

-- Most played game by hours
SELECT games.title, SUM(user_library.hours_played) AS total_hours
FROM user_library
JOIN games ON user_library.game_id = games.game_id
GROUP BY games.title
ORDER BY total_hours DESC
LIMIT 1;

-- Completed games
SELECT users.username, games.title
FROM user_library
JOIN users ON user_library.user_id = users.user_id
JOIN games ON user_library.game_id = games.game_id
WHERE user_library.status = 'completed';

-- How many game each user has
SELECT users.username, COUNT(user_library.game_id) AS total_games
FROM user_library
JOIN users ON user_library.user_id = users.user_id
GROUP BY users.username;

-- AVG hours per game
SELECT games.title, AVG(user_library.hours_played) AS avg_hours
FROM user_library
JOIN games ON user_library.game_id = games.game_id
GROUP BY games.title;
