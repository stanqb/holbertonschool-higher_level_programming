-- Script that creates the table force_name
-- With id INT and name VARCHAR(256) that can't be null
-- If the table already exists, the script should not fail
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
