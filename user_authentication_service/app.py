#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request, abort, make_response
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


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ POST a user
    Return:
      - JSON message
    """
    email = request.form['email']
    password = request.form['password']
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """Login function to respond to POST /sessions"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        abort(401)

    if not AUTH.valid_login(email, password):
        abort(401)

    user = AUTH.current_user(request)
    if user is None:
        abort(401)

    session_id = AUTH.create_session(user.id)
    response = make_response(jsonify({"message": "Logged in"}))
    response.set_cookie("session_id", session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
