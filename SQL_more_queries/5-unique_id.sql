-- Script that creates the table unique_id
-- With id INT default 1 and unique, and name VARCHAR(256)
-- If the table already exists, the script should not fail
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
