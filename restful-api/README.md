# RESTful API Project

## Description
This project explores the fundamentals of RESTful APIs, covering everything from basic HTTP/HTTPS concepts to advanced API development and security implementation. It provides hands-on experience with various tools and technologies commonly used in API development and consumption.

## Learning Objectives
- Understand HTTP/HTTPS protocols and their differences
- Master API consumption using command-line tools (curl)
- Develop proficiency in API consumption using Python
- Create basic APIs using Python's built-in `http.server`
- Build sophisticated APIs using Flask framework
- Implement API security and authentication
- Learn API documentation standards

## Project Structure
The project consists of several tasks, each focusing on different aspects of API development:

### 1. HTTP/HTTPS Basics
- Understanding the fundamental differences between HTTP and HTTPS
- Learning about HTTP request/response structure
- Exploring common HTTP methods and status codes

### 2. curl for API Consumption
- Installing and using curl
- Making basic API requests
- Working with headers and different HTTP methods
- Interpreting API responses

### 3. Python Requests for API Consumption
- Using the `requests` library
- Fetching and processing API data
- Converting API responses to different formats

### 4. Basic API Development with http.server
- Creating a simple HTTP server
- Handling different endpoints
- Serving JSON responses

### 5. Flask API Development
- Building a RESTful API using Flask
- Implementing various endpoints
- Handling different HTTP methods
- Managing data storage and retrieval

### 6. API Security Implementation
- Basic authentication
- Token-based authentication (JWT)
- Role-based access control
- Secure route protection

## Requirements
- Python 3.x
- Flask
- requests library
- curl
- Flask-HTTPAuth
- Flask-JWT-Extended

## Installation
```bash
# Clone the repository
git clone [repository-url]

# Navigate to the project directory
cd restful-api

# Install required Python packages
pip install flask requests flask-httpauth flask-jwt-extended
```

## Usage
Each task can be run independently:

### HTTP/HTTPS Understanding
```bash
# No specific commands - theoretical understanding
```

### Using curl
```bash
# Basic curl command
curl http://example.com

# Making a POST request
curl -X POST -d "data=value" http://api-endpoint
```

### Python Requests
```bash
# Run the requests example
python task_02_requests.py
```

### HTTP Server
```bash
# Start the basic HTTP server
python task_03_http_server.py
```

### Flask API
```bash
# Run the Flask application
flask --app task_04_flask.py run
```

### Security Implementation
```bash
# Run the secured API
python task_05_basic_security.py
```

## File Structure
```
restful-api/
│
├── task_02_requests.py      # Python requests implementation
├── task_03_http_server.py   # Basic HTTP server
├── task_04_flask.py         # Flask API implementation
├── task_05_basic_security.py # Security implementation
└── README.md
```

## API Documentation

### Basic Endpoints
- `GET /` - Welcome message
- `GET /data` - Retrieve sample data
- `GET /status` - Check API status
- `GET /users/<username>` - Get user information
- `POST /add_user` - Add new user

### Protected Endpoints
- `GET /basic-protected` - Basic auth protected route
- `POST /login` - JWT token generation
- `GET /jwt-protected` - JWT protected route
- `GET /admin-only` - Admin role protected route

## Contributing
This is an educational project. While contributions are welcome, please ensure you follow the existing code structure and documentation standards.

## License
This project is part of the Holberton School learning program.

## Author
Stan QUEUNIEZ

## Acknowledgments
- Holberton School for the project structure and requirements
- Flask documentation and community
- Python requests library documentation
