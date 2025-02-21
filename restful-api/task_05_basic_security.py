from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (JWTManager, create_access_token,
                                jwt_required, get_jwt_identity)
import os

# Crée une instance de Flask
app = Flask(__name__)
auth = HTTPBasicAuth()

# Utilisation d'une variable d'environnement pour la clé secrète JWT
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "default_jwt_secret_key")
jwt = JWTManager(app)

# Dictionnaire d'utilisateurs, à déplacer vers un modèle dans un vrai projet
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# Vérification des informations d'authentification basiques
@auth.verify_password
def verify_password(username, password):
    """
    Vérifie le nom d'utilisateur et le mot de passe pour l'authentification basique.

    Args:
        username (str): Le nom d'utilisateur à vérifier.
        password (str): Le mot de passe à vérifier.

    Returns:
        dict ou None: Le dictionnaire de l'utilisateur si les informations sont
        valides, None sinon.
    """
    if username in users and check_password_hash(
            users[username]["password"], password):
        return username
    return None


# Route protégée par une authentification basique
@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Point de terminaison protégé par une authentification basique.

    Returns:
        str: Un message indiquant l'accès accordé.
    """
    return "Basic Auth: Access Granted"


# Route de connexion pour générer un token JWT
@app.route('/login', methods=['POST'])
def login():
    """
    Point de terminaison pour la connexion utilisateur et la génération du token JWT.

    Returns:
        flask.Response: Réponse JSON avec le token d'accès ou un message d'erreur.
    """
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Invalid username or password"}), 401

    username = data['username']
    password = data['password']

    if username in users and check_password_hash(
            users[username]["password"], password):
        access_token = create_access_token(
            identity={
                "username": username,
                "role": users[username]["role"]
            }
        )
        return jsonify({"access_token": access_token})

    return jsonify({"error": "Invalid credentials"}), 401


# Route protégée par un token JWT
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    Point de terminaison protégé par une authentification JWT.

    Returns:
        str: Un message indiquant l'accès accordé.
    """
    return "JWT Auth: Access Granted"


# Route réservée aux administrateurs
@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    Point de terminaison accessible uniquement aux utilisateurs avec le rôle admin.

    Returns:
        str ou flask.Response: Un message de succès ou une réponse d'erreur.
    """
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"
