CREATE TABLE IF NOT EXISTS users (
    username varchar(255) NOT NULL UNIQUE primary key,
    password varchar(255) NOT NULL
);
