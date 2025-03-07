-- Script that creates the database hbtn_0d_usa and the table states
-- states has id INT unique, auto generated, can't be null and is primary key
-- and name VARCHAR(256) can't be null
-- If the database or table already exists, script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
