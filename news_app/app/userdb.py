import sqlite3

conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

cursor.execute ("""CREATE TABLE users (
    user_id INTEGER PRIMARY KEY NOT NULL UNIQUE CHECK(length(user_id) <= 100),
    first_name TEXT NOT NULL CHECK(length(first_name) <= 100),
    last_name TEXT CHECK(length(user_id) <= 50),
   user_name TEXT NOT NULL UNIQUE CHECK(length(user_id) <= 25),
    email TEXT NOT NULL UNIQUE ,
    password TEXT NOT NULL,
   followers INTEGER,
    pfp BLOB,
    causes TEXT NOT NULL,
    FOREIGN KEY (user_name) REFERENCES users(user_name)
);
""")
