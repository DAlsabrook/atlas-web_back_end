#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def status() -> str:
    """ GET /
    Return:
      - JSON payload with a welcome message
    """
    return jsonify({"message": "Bienvenue"})



@app.route('/users', methods=['POST'])
def users(email: str, password: str) -> str:
    """ POST a user
    Return:
      - JSON message
    """
    try:
      user = AUTH.register_user(email, password)
      return jsonify({"email": email, "message": "user created"})
    except ValueError:
      return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
