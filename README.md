<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
</head>
<body>

<h1>🎮 Steam Tracker</h1>

<p>
Steam Tracker is a Python + MySQL application for tracking users, games, and game libraries.
It uses a menu-driven CLI and a relational database to manage users, games, playtime, and game status.
</p>

<hr>

<h2>Features</h2>
<ul>
  <li><strong>User Management:</strong> Add and delete users (with automatic library cleanup).</li>
  <li><strong>Game Management:</strong> Add games with title, developer, release year, and price.</li>
  <li><strong>User Library:</strong> Track each user's games, status, and playtime.</li>
  <li><strong>Safe SQL Transactions:</strong> Used for user deletion and library updates.</li>
  <li><strong>View Full User Libraries:</strong> Joined data of all games owned by all users.</li>
</ul>

<hr>

<h2>Project Structure</h2>
<pre>
/steam-tracker
│
├── main.py              # CLI logic
├── database.py          # Database operations
├── README.md            # Documentation
├── requirements.txt     # Python dependencies
│
├── schema.sql           # Database schema (tables + constraints)
├── data.sql             # Sample data
├── queries.sql          # Example queries for testing/demo
│
└── ERD.png              # Entity Relationship Diagram
</pre>

<hr>

<h2>Entity Relationship Diagram (ERD)</h2>
<p>
This diagram visualizes how users, games, libraries, genres, and achievements relate to each other.
</p>

<img src="ERD.png" alt="Steam Tracker ERD" width="800">

<hr>

<h2>SQL Files</h2>

<h3><code>schema.sql</code></h3>
<p>
Contains all <strong>CREATE TABLE</strong> statements including:
<ul>
  <li>Primary keys</li>
  <li>Foreign keys</li>
  <li>Constraints</li>
  <li>Cascade delete behavior</li>
</ul>
</p>

<h3><code>data.sql</code></h3>
<p>
Provides sample data for testing:
<ul>
  <li>Users</li>
  <li>Games</li>
  <li>User libraries</li>
  <li>Genres</li>
  <li>Achievements</li>
</ul>
</p>

<h3><code>queries.sql</code></h3>
<p>
Includes useful queries such as:
<ul>
  <li>Viewing all user libraries (JOINs)</li>
  <li>Filtering by status (wishlist, owned, etc.)</li>
  <li>Playtime reports</li>
  <li>Update examples</li>
</ul>
</p>

<hr>

<h2>Database Schema Overview</h2>

<h3>1. <code>users</code></h3>
<table border="1" cellpadding="5">
<tr><th>Column</th><th>Type</th><th>Description</th></tr>
<tr><td>user_id</td><td>INT AUTO_INCREMENT</td><td>Primary Key</td></tr>
<tr><td>username</td><td>VARCHAR(255)</td><td>User name</td></tr>
<tr><td>email</td><td>VARCHAR(255)</td><td>User email</td></tr>
</table>

<h3>2. <code>games</code></h3>
<table border="1" cellpadding="5">
<tr><th>Column</th><th>Type</th><th>Description</th></tr>
<tr><td>game_id</td><td>INT AUTO_INCREMENT</td><td>Primary Key</td></tr>
<tr><td>title</td><td>VARCHAR(255)</td><td>Game title</td></tr>
<tr><td>developer</td><td>VARCHAR(255)</td><td>Developer</td></tr>
<tr><td>release_year</td><td>INT</td><td>Release year</td></tr>
<tr><td>price</td><td>DECIMAL(6,2)</td><td>Price</td></tr>
</table>

<h3>3. <code>user_library</code></h3>
<table border="1" cellpadding="5">
<tr><th>Column</th><th>Type</th><th>Description</th></tr>
<tr><td>user_id</td><td>INT</td><td>FK → users</td></tr>
<tr><td>game_id</td><td>INT</td><td>FK → games</td></tr>
<tr><td>status</td><td>VARCHAR(50)</td><td>wishlist, owned, playing, completed</td></tr>
<tr><td>hours_played</td><td>INT</td><td>Playtime</td></tr>
</table>

<h3>4. <code>genres</code></h3>
<table border="1" cellpadding="5">
<tr><th>Column</th><th>Type</th><th>Description</th></tr>
<tr><td>genre_id</td><td>INT AUTO_INCREMENT</td><td>Primary Key</td></tr>
<tr><td>genre_name</td><td>VARCHAR(255)</td><td>Genre name</td></tr>
</table>

<h3>5. <code>game_genres</code></h3>
<table border="1" cellpadding="5">
<tr><th>Column</th><th>Type</th><th>Description</th></tr>
<tr><td>game_id</td><td>INT</td><td>FK → games</td></tr>
<tr><td>genre_id</td><td>INT</td><td>FK → genres</td></tr>
<tr><td>PRIMARY KEY</td><td>(game_id, genre_id)</td><td>Composite key</td></tr>
</table>

<h3>6. <code>achievements</code></h3>
<table border="1" cellpadding="5">
<tr><th>Column</th><th>Type</th><th>Description</th></tr>
<tr><td>achievement_id</td><td>INT AUTO_INCREMENT</td><td>Primary Key</td></tr>
<tr><td>game_id</td><td>INT</td><td>FK → games</td></tr>
<tr><td>title</td><td>VARCHAR(255)</td><td>Achievement name</td></tr>
<tr><td>description</td><td>TEXT</td><td>Description</td></tr>
<tr><td>points</td><td>INT</td><td>Score value</td></tr>
</table>

<hr>

<h2>Installation & Setup</h2>

<h3>1. Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>2. MySQL Setup</h3>

<pre>
CREATE DATABASE steam_tracker;
USE steam_tracker;
</pre>

<p>Run schema:</p>
<pre>
SOURCE schema.sql;
</pre>

<p>Optional sample data:</p>
<pre>
SOURCE data.sql;
</pre>

<hr>

<h2>Running the Program</h2>

<pre>
python main.py
</pre>

<pre>
🎮 Steam Tracker
1. Add User
2. Add Game
3. Delete User + Library
4. Add Game to Library + Set Status
5. View All User Libraries
6. Update Playtime
7. Exit
</pre>

<hr>

<h2>Feature Breakdown</h2>

<h3>Add User</h3>
<p>Creates a new user.</p>

<h3>Add Game</h3>
<p>Adds a new game.</p>

<h3>Delete User + Library</h3>
<p>Uses transactions to safely remove user and related data.</p>

<h3>Add Game to Library</h3>
<p>Adds a game and updates status (wishlist → owned supported).</p>

<h3>View Libraries</h3>
<p>Displays all users and their games using JOIN queries.</p>

<h3>Update Playtime</h3>
<p>Updates hours played.</p>

<hr>

<h2>Error Handling</h2>
<ul>
  <li>Input validation (ValueError)</li>
  <li>MySQL connection errors</li>
  <li>Transaction rollback</li>
  <li>Clear debug messages</li>
</ul>

<hr>

<h2>Future Improvements</h2>
<ul>
  <li>CSV export</li>
  <li>GUI (Tkinter / PyQt)</li>
  <li>Steam API integration</li>
  <li>Filtering & sorting</li>
</ul>

<hr>

</body>
</html>
