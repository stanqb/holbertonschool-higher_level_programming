-- Script that creates the MySQL server user user_0d_1 with all privileges
-- Create user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- Apply privileges
FLUSH PRIVILEGES;
