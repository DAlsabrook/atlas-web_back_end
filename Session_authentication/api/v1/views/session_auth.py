#!/usr/bin/env python3
"""
Routes for session auth
"""
from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400
    user = User.search({"email": email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    response = make_response(user.to_json())
    response.set_cookie(os.getenv('SESSION_NAME',
                                  '_my_session_id'), session_id)
    return response


@app_views.route('/api/v1/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """Logout user from session

    Returns:
        str: _description_
    """
    from api.v1.app import auth
    removed = auth.destroy_session(request)
    if removed:
        abort(404)
    return jsonify({}), 200
