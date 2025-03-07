-- Script that creates the MySQL server user user_0d_1 with all privileges
-- and password user_0d_1_pwd. If the user already exists, the script will not fail.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;