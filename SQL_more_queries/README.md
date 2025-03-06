# SQL - More Queries

## Description
This project focuses on advanced MySQL database queries and management concepts. It covers essential database administration skills including user creation, privilege management, and advanced query techniques like subqueries and joins.

## Learning Objectives
By the end of this project, you should be able to explain:

### User Management
- How to create a new MySQL user
- How to manage privileges for users in databases and tables

### Database Constraints & Design
- What is a PRIMARY KEY and its importance
- What is a FOREIGN KEY and how to implement relationships
- How to use NOT NULL and UNIQUE constraints

### Advanced Queries
- How to retrieve data from multiple tables in one request
- What are subqueries and when to use them
- How to use JOIN operations (INNER JOIN, LEFT JOIN, etc.)
- When to use UNION operations

## Tasks Overview

0. **My privileges!** - Write a script that lists all privileges of MySQL users user_0d_1 and user_0d_2.

1. **Root user** - Create a MySQL server user with all privileges.

2. **Read user** - Create a database and a user with only SELECT privilege on that database.

3. **Always a name** - Create a table with a NOT NULL constraint.

4. **ID can't be null** - Create a table with a default value.

5. **Unique ID** - Create a table with a UNIQUE constraint.

6. **States table** - Create a database and a table with a PRIMARY KEY.

7. **Cities table** - Create a table with a FOREIGN KEY.

8. **Cities of California** - Write a subquery to list cities from a specific state.

9. **Cities by States** - Use a JOIN to list cities with their state names.

10. **Genre ID by show** - Query data from multiple tables with relationships.

11. **Genre ID for all shows** - Use LEFT JOIN to include records without matches.

12. **No genre** - Filter records that don't have related data in another table.

13. **Number of shows by genre** - Count and group data from related tables.

14. **My genres** - Use multiple JOINs to follow table relationships.

15. **Only Comedy** - Filter by specific genre using table relationships.

16. **List shows and genres** - Create a comprehensive listing using multiple JOINs.

## Requirements
- All scripts must be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All files should end with a new line
- All SQL queries should have a comment just before explaining the task
- All SQL keywords should be in uppercase (SELECT, WHERE, etc.)
- Files will be tested using wc

## Key Concepts Explained

### PRIMARY KEY
A PRIMARY KEY is a column or set of columns that uniquely identifies each row in a table. It enforces entity integrity and cannot contain NULL values. Each table can have only one PRIMARY KEY.

### FOREIGN KEY
A FOREIGN KEY is a field (or collection of fields) in one table that refers to the PRIMARY KEY in another table. It creates a link between the two tables and maintains referential integrity.

### JOINs vs UNIONs
- **JOIN**: Combines rows from two or more tables based on a related column between them.
  - INNER JOIN: Returns records with matching values in both tables
  - LEFT JOIN: Returns all records from the left table and matched records from the right table
  - RIGHT JOIN: Returns all records from the right table and matched records from the left table

- **UNION**: Combines the result sets of two or more SELECT statements into a single result set. The SELECT statements must have the same number of columns with compatible data types.

### Subqueries
A subquery is a query nested inside another query. It can be used in various parts of a SQL statement:
- In the WHERE clause to filter results
- In the FROM clause as a derived table
- In the SELECT clause as a scalar value

## Author
Stan QUEUNIEZ - [Holberton School](https://www.holbertonschool.com)
