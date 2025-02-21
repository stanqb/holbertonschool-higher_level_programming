#!/usr/bin/python3

"""
Simple API using Python & Flask
"""

from flask import Flask, jsonify, request

# Create a Flask application
app = Flask(__name__)

# User dictionary for tests :
users = {}


@app.route("/")
def home():
    """
    Home Default root URL

    Will return a simple message
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """
    get_data

    Get data from /data

    Returns:
       dict: A dictionary containing the usernames
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """
    get_status
    Get status from /status

    Returns:
        str : OK
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    get_user

    Args:
        username (str): username to get

    Returns:
        user data
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    add_user

    add user with POST method

    Returns:
       user data successfully added
    """
    retrieved_data = request.get_json()

    # Check if dictionary contains a username key
    if not retrieved_data or "username" not in retrieved_data:
        return jsonify({"error": "Username is required"}), 400

    username = retrieved_data["username"]
    users[username] = retrieved_data

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
