-- Script that creates the table id_not_null
-- With id INT with default value 1 and name VARCHAR(256)
-- If the table already exists, the script should not fail
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
