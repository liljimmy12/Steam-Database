
USE steam_tracker;

INSERT INTO users (username, email) VALUES
('johndoe', 'johndoe@gmail.com'),
('janesmith', 'janesmith@yahoo.com'),
('michaelb', 'michaelb@hotmail.com'),
('emilyclark', 'emily.clark@gmail.com'),
('davidlee', 'david.lee@yahoo.com'),
('sarahw', 'sarahw@gmail.com'),
('chrisjohnson', 'chris.johnson@outlook.com'),
('ashleytaylor', 'ashley.taylor@gmail.com'),
('danielmartin', 'daniel.martin@yahoo.com'),
('oliviabrown', 'olivia.brown@gmail.com');

INSERT INTO games (title, developer, release_year, price) VALUES
('Elden Ring', 'FromSoftware', 2022, 59.99),
('Minecraft', 'Mojang', 2011, 29.99),
('Cyberpunk 2077', 'CD Projekt Red', 2020, 59.99),
('Stardew Valley', 'ConcernedApe', 2016, 14.99),
('Call of Duty: Modern Warfare', 'Infinity Ward', 2019, 59.99),
('Terraria', 'Re-Logic', 2011, 9.99),
('The Witcher 3', 'CD Projekt Red', 2015, 39.99),
('Grand Theft Auto V', 'Rockstar Games', 2013, 29.99),
('Hades', 'Supergiant Games', 2020, 24.99),
('Counter-Strike 2', 'Valve', 2023, 0.00);

INSERT INTO genres (genre_name) VALUES
('RPG'),
('FPS'),
('Sandbox'),
('Adventure'),
('Action'),
('Simulation'),
('Open World'),
('Indie'),
('Strategy'),
('Roguelike');

INSERT INTO game_genres (game_id, genre_id) VALUES
(1,1),(1,5),
(2,3),(2,4),
(3,1),(3,7),
(4,6),(4,8),
(5,2),(5,5),
(6,3),(6,8),
(7,1),(7,7),
(8,5),(8,7),
(9,5),(9,10),
(10,2),(10,5);

INSERT INTO user_library (user_id, game_id, hours_played, status) VALUES
(1,1,120,'completed'),
(1,2,45,'playing'),
(2,3,30,'playing'),
(2,4,80,'completed'),
(3,5,60,'playing'),
(4,6,25,'wishlist'),
(5,7,200,'completed'),
(6,8,150,'completed'),
(7,9,40,'playing'),
(8,10,300,'completed'),
(9,1,10,'playing'),
(10,2,5,'wishlist');

INSERT INTO achievements (game_id, name, description) VALUES
(1,'First Boss','Defeat your first boss'),
(1,'Elden Lord','Complete the game'),
(2,'Getting Wood','Punch a tree for the first time'),
(2,'Diamond Miner','Acquire diamonds'),
(3,'The Heist','Complete the first major mission'),
(4,'Greenhorn','Reach level 10 farming'),
(5,'First Blood','Get your first kill'),
(6,'Survivor','Survive your first night'),
(7,'Monster Slayer','Defeat 100 enemies'),
(9,'Escape the Underworld','Beat the final boss');