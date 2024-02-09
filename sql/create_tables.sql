-- Start by deleting any tables if the exist already
-- We want to be able to re-run this script as needed.
-- DROP tables in reverse order of creation 
-- DROP dependent tables (with foreign keys) first

DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Posts;

-- Create Users Table
CREATE TABLE IF NOT EXISTS Users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  username VARCHAR(255) UNIQUE,
  email VARCHAR(255) UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the Post table
CREATE TABLE IF NOT EXISTS Posts (
  post_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  title VARCHAR(255),
  content TEXT,
  published_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);