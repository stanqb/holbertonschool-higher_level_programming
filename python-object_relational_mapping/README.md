# Python Object-Relational Mapping

This project explores the connection between databases and Python using both MySQLdb and SQLAlchemy ORM.

## Description

This project implements various scripts to interact with MySQL databases through Python, covering:
- Basic SQL operations using MySQLdb module
- ORM implementation using SQLAlchemy
- Creating, updating, and deleting database records
- SQL injection prevention
- Querying related tables with joins

## Technologies

- Python 3.8.5
- MySQL 8.0
- MySQLdb 2.0.x (Python module)
- SQLAlchemy 1.4.x (Python ORM)

## Requirements

- Ubuntu 20.04 LTS
- Python 3.8.5
- MySQL 8.0
- pycodestyle 2.7.* (for code style checking)

## Installation

```bash
# Install MySQL
sudo apt update
sudo apt install mysql-server

# Install MySQLdb module
sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install zlib1g-dev
sudo pip3 install mysqlclient

# Install SQLAlchemy
sudo pip3 install SQLAlchemy
```

## File Structure

- **Task 0-5**: Direct MySQL manipulation with MySQLdb
  - `0-select_states.py`: Lists all states from a database
  - `1-filter_states.py`: Lists states starting with 'N'
  - `2-my_filter_states.py`: Lists states matching a parameter
  - `3-my_safe_filter_states.py`: Same as task 2, but safe from SQL injection
  - `4-cities_by_state.py`: Lists all cities
  - `5-filter_cities.py`: Lists cities by state

- **Task 6-14**: ORM with SQLAlchemy
  - `model_state.py`: State class definition
  - `7-model_state_fetch_all.py`: Lists all State objects
  - `8-model_state_fetch_first.py`: Displays the first State
  - `9-model_state_filter_a.py`: Lists states containing 'a'
  - `10-model_state_my_get.py`: Gets a state by name
  - `11-model_state_insert.py`: Adds a new state
  - `12-model_state_update_id_2.py`: Updates a state
  - `13-model_state_delete_a.py`: Deletes states containing 'a'
  - `model_city.py`: City class definition
  - `14-model_city_fetch_by_state.py`: Lists cities by state

## Usage

Scripts generally follow this execution pattern:

```bash
./[script_name].py [mysql_username] [mysql_password] [database_name] [additional_args]
```

Example:
```bash
./0-select_states.py root root hbtn_0e_0_usa
```

## License

This project is part of the Holberton School curriculum.
