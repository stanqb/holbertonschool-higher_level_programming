# SQL Introduction

## Project Overview

This project serves as a comprehensive introduction to SQL (Structured Query Language) and relational database management using MySQL 8.0. Through a series of progressive tasks, you'll learn how to create, manipulate, and query databases, gaining essential skills for data management and retrieval.

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without external help:

### General Concepts
- **Database**: A structured collection of data organized for efficient storage, retrieval, and management
- **Relational Database**: A type of database that stores and provides access to data points that are related to one another, organized in tables with rows and columns
- **SQL (Structured Query Language)**: The standard language for interacting with relational databases
- **MySQL**: An open-source relational database management system
- **Database Creation**: The process of defining and instantiating a new database structure
- **DDL (Data Definition Language)**: SQL commands that define the database structure (CREATE, ALTER, DROP)
- **DML (Data Manipulation Language)**: SQL commands that manipulate data (SELECT, INSERT, UPDATE, DELETE)
- **Table Management**: Creating, altering, and managing database tables
- **Data Retrieval**: Selecting and filtering data from tables
- **Data Modification**: Inserting, updating, and deleting data
- **Subqueries**: Nested queries within a larger SQL statement
- **MySQL Functions**: Built-in functions for data transformation and manipulation

## Technical Requirements

- **Environment**: All files will be executed on Ubuntu 20.04 LTS
- **MySQL Version**: MySQL 8.0 (version 8.0.25)
- **File Format**: All files should end with a new line
- **Documentation**: Each SQL query must be preceded by a comment describing its purpose
- **File Headers**: All files should start with a comment describing the task
- **SQL Syntax**: All SQL keywords must be in uppercase (SELECT, WHERE, etc.)
- **Code Quality**: The length of files will be tested using `wc`

## Environment Setup

### Setting up MySQL 8.0 on Ubuntu 20.04 LTS

```bash
# Update package repositories
$ sudo apt update

# Install MySQL server
$ sudo apt install mysql-server

# Verify installation
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))

# Start MySQL service (if not already running)
$ sudo service mysql start
```

### Connecting to MySQL Server

```bash
# Connect with authentication
$ mysql -uroot -p
Enter password: 

# Or, if using sudo
$ sudo mysql

# You should see the MySQL prompt
mysql>
```

## Database Sandbox Options

### For Ubuntu 22.04 (Current image on CoD Platform)
1. Request a container with Ubuntu 22.04
2. Update package list: `apt update`
3. Install MySQL server: `apt install -y mysql-server`
4. Verify installation: `mysql --version`
5. Start MySQL service: `service mysql start`
6. Connect to MySQL: `mysql -uroot`

### For Ubuntu 20.04 Sandbox
1. Request a container with Ubuntu 20.04
2. Connect via SSH or Web terminal
3. Start MySQL service: `service mysql start`
4. Connect to MySQL: `mysql -uroot -p` (credentials: root/root)

## Project Tasks

The project consists of 17 progressive tasks that build your SQL skills:

### Basic Database Operations (Tasks 0-3)
- **0. List databases**: Script to list all databases on the MySQL server
- **1. Create a database**: Create the database `hbtn_0c_0` if it doesn't exist
- **2. Delete a database**: Remove the database `hbtn_0c_0` if it exists
- **3. List tables**: Display all tables in a specified database

### Table Management (Tasks 4-6)
- **4. First table**: Create a table called `first_table` with id and name columns
- **5. Full description**: Display the complete structure of `first_table`
- **6. List all in table**: List all rows from `first_table`

### Data Manipulation (Tasks 7-9)
- **7. First add**: Insert a new row with id=89 and name="Best School"
- **8. Count 89**: Count records with id=89 in `first_table`
- **9. Full creation**: Create `second_table` and add multiple records with id, name, and score

### Data Querying (Tasks 10-16)
- **10. List by best**: List records ordered by score (highest first)
- **11. Select the best**: List records with score >= 10
- **12. Cheating is bad**: Update Bob's score to 10
- **13. Score too low**: Remove records with score <= 5
- **14. Average**: Calculate the average score of all records
- **15. Number by score**: List the number of records for each score
- **16. Say my name**: List records with non-empty name values

## Repository Structure

```
SQL_introduction/
├── 0-list_databases.sql          # Lists all databases
├── 1-create_database_if_missing.sql  # Creates a database
├── 2-remove_database.sql         # Deletes a database
├── 3-list_tables.sql             # Lists all tables of a database
├── 4-first_table.sql             # Creates a table
├── 5-full_table.sql              # Shows table description
├── 6-list_values.sql             # Lists all rows of a table
├── 7-insert_value.sql            # Inserts a new row
├── 8-count_89.sql                # Counts records with specific criteria
├── 9-full_creation.sql           # Creates a table with multiple rows
├── 10-top_score.sql              # Lists records by score
├── 11-best_score.sql             # Lists records with score >= 10
├── 12-no_cheating.sql            # Updates a score
├── 13-change_class.sql           # Removes records with score <= 5
├── 14-average.sql                # Computes average score
├── 15-groups.sql                 # Lists records grouped by score
├── 16-no_link.sql                # Lists records with non-empty names
└── README.md                     # Project documentation
```

## Execution Examples

### Example 1: Listing Databases
```bash
$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
mysql
performance_schema
sys
```

### Example 2: Creating and Populating a Table
```bash
# Create the table
$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 

# Verify the data
$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14      Bob
10      John
8       George
3       Alex
```

## Key SQL Concepts

### Data Definition Language (DDL)
- **CREATE**: Creates database objects like databases, tables
- **ALTER**: Modifies existing database objects
- **DROP**: Removes database objects
- **TRUNCATE**: Removes all records from a table

### Data Manipulation Language (DML)
- **SELECT**: Retrieves data from a database
- **INSERT**: Adds new data to a table
- **UPDATE**: Modifies existing data
- **DELETE**: Removes data from a table

### Common SQL Functions
- **Aggregate Functions**: COUNT(), SUM(), AVG(), MIN(), MAX()
- **String Functions**: CONCAT(), SUBSTRING(), TRIM(), UPPER(), LOWER()
- **Date Functions**: NOW(), CURDATE(), DATE_FORMAT(), DATEDIFF()
- **Mathematical Functions**: ROUND(), CEIL(), FLOOR(), ABS()

## Best Practices

1. Always backup your database before making significant changes
2. Use meaningful table and column names
3. Comment your SQL code for clarity
4. Use appropriate data types for columns
5. Apply constraints (PRIMARY KEY, FOREIGN KEY, etc.) to maintain data integrity
6. Use parameterized queries when working with user input to prevent SQL injection


## Author

- Stan QUEUNIEZ

## License

This project is licensed under the terms of Holberton School.
