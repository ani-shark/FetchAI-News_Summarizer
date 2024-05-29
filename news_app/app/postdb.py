import sqlite3

conn = sqlite3.connect('posts_database.db')
cursor = conn.cursor()


conn = sqlite3.connect('posts_database.db')
cursor = conn.cursor()

create_posts_table_query = """
CREATE TABLE posts (
    post_id TEXT UNIQUE NOT NULL,
    user_name TEXT NOT NULL UNIQUE,
    heading TEXT NOT NULL ,
    description TEXT(500),
    body TEXT(1500) NOT NULL,
    images BLOB,
    videos BLOB,
    lat INTEGER NOT NULL,
    lang INTEGER NOT NULL,
    choice TEXT(255),
    duration INTEGER NOT NULL,
    comments TEXT(255),
    privacy BOOLEAN NOT NULL,
    FOREIGN KEY (user_name) REFERENCES users(user_name)
);"""

cursor.execute(create_posts_table_query)


conn.commit()
conn.close()
