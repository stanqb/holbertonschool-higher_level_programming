-- Script that creates the database hbtn_0d_usa and the table cities
-- cities has id INT unique, auto generated, can't be null and is primary key
-- state_id INT, can't be null and must be a FOREIGN KEY that references to id of states
-- and name VARCHAR(256) can't be null
-- If the database or table already exists, script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
