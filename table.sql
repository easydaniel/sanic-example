CREATE TABLE IF NOT EXISTS users (
    username varchar(255) NOT NULL UNIQUE PRIMARY KEY,
    password varchar(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS pays (
    id SERIAL PRIMARY KEY,
    owner varchar(255) NOT NULL,
    borrower varchar(255) NOT NULL,
    money integer NOT NULL
);
