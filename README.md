<h1>Steam Tracker</h1>

<p>
Steam Tracker is a Python + MySQL application for tracking users, games, and game libraries.
It uses a menu-driven CLI and a relational database to manage users, games, playtime, and game status.
</p>

<hr>

<h2>Features</h2>
<ul>
  <li><strong>User Management:</strong> Add and delete users (with automatic library cleanup).</li>
  <li><strong>Game Management:</strong> Add games with title, developer, release year, and price.</li>
  <li><strong>User Library:</strong> Track each user's games, status, playtime.</li>
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
└── requirements.txt     # Python dependencies
</pre>

<hr>

<h2>Database Schema</h2>

<h3>1. <code>users</code> Table</h3>
<table>
<tr><th>Column</th><th>Type</th><th>Description</th></tr>
<tr><td>user_id</td><td>INT AUTO_INCREMENT</td><td>Primary Key</td></tr>
<tr><td>username</td><td>VARCHAR(255)</td><td>User name</td></tr>
<tr><td>email</td><td>VARCHAR(255)</td><td>User email</td></tr>
</table>

<h3>2. <code>games</code> Table</h3>
<table>
<tr><th>Column</th><th>Type</th><th>Description</th></tr>
<tr><td>game_id</td><td>INT AUTO_INCREMENT</td><td>Primary Key</td></tr>
<tr><td>title</td><td>VARCHAR(255)</td><td>Game title</td></tr>
<tr><td>developer</td><td>VARCHAR(255)</td><td>Studio/Developer</td></tr>
<tr><td>release_year</td><td>INT</td><td>Year released</td></tr>
<tr><td>price</td><td>DECIMAL(6,2)</td><td>Game price</td></tr>
</table>

<h3>3. <code>user_library</code> Table</h3>
<table>
<tr><th>Column</th><th>Type</th><th>Description</th></tr>
<tr><td>user_id</td><td>INT</td><td>Foreign Key → users.user_id</td></tr>
<tr><td>game_id</td><td>INT</td><td>Foreign Key → games.game_id</td></tr>
<tr><td>status</td><td>VARCHAR(50)</td><td>wishlist, owned, playing, completed</td></tr>
<tr><td>hours_played</td><td>INT</td><td>Total hours played</td></tr>
</table>

<hr>

<h2>Installation & Setup</h2>

<h3>1. Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>2. MySQL Setup</h3>

<p>Create the database:</p>
<pre>
CREATE DATABASE steam_tracker;
USE steam_tracker;
</pre>

<p>Create the tables:</p>
<pre>
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255),
    email VARCHAR(255)
);

CREATE TABLE games (
    game_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    developer VARCHAR(255),
    release_year INT,
    price DECIMAL(6,2)
);

CREATE TABLE user_library (
    user_id INT,
    game_id INT,
    status VARCHAR(50) DEFAULT 'wishlist',
    hours_played INT DEFAULT 0,
    PRIMARY KEY (user_id, game_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (game_id) REFERENCES games(game_id)
);
</pre>

<hr>

<h2>Running the Program</h2>

<pre>
python main.py
</pre>

<p>You will see this menu:</p>

<pre>
 Steam Tracker
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

<h3>1. Add User</h3>
<p>Creates a new user with username + email.</p>

<h3>2. Add Game</h3>
<p>Adds a new game with title, developer, release year, and price.</p>

<h3>3. Delete User + Library</h3>
<p>
Uses a SQL transaction to:<br>
1️⃣ Delete all user_library entries<br>
2️⃣ Delete user<br>
3️⃣ Commit or roll back safely
</p>

<h3>4. Add Game to Library + Status</h3>
<p>
Adds a game to a user's library and immediately updates its status.
Handled using SQL transactions.
</p>

<h3>5. View All Libraries</h3>
<p>Displays a joined list of all users and their games:</p>

<pre>
User: Alice | Game: Halo | Hours: 25
User: Bob   | Game: Doom | Hours: 14
</pre>

<h3>6. Update Playtime</h3>
<p>Updates <code>hours_played</code> for a specific user + game.</p>

<hr>

<h2>Error Handling</h2>
<ul>
  <li>Invalid input type handling (ValueError)</li>
  <li>MySQL connection errors</li>
  <li>Transaction rollback on failure</li>
  <li>Clear error messages for debugging</li>
</ul>

<hr>

<h2>Future Improvements</h2>
<ul>
  <li>Add CSV export</li>
  <li>Add GUI (Tkinter / PyQt)</li>
  <li>Add API integration (e.g., Steam API)</li>
  <li>Add sorting/filtering options</li>
</ul>
