DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

INSERT INTO user (username, password) VALUES ('admin', 'adminpass');
INSERT INTO user (username, password) VALUES ('user1', 'user1pass');

INSERT INTO post (author_id, title, body) VALUES (1, 'Welcome to the Blog', 'This is the first post on the blog!');
INSERT INTO post (author_id, title, body) VALUES (2, 'Hello World', 'Excited to join this blogging platform!'); 