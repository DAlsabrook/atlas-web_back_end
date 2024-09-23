#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request, make_response
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None
auth_type = getenv('AUTH_TYPE')

if auth_type:
    if auth_type == 'auth':
        from api.v1.auth.auth import Auth
        auth = Auth()
    if auth_type == 'basic_auth':
        from api.v1.auth.basic_auth import BasicAuth
        auth = BasicAuth()
    if auth_type == 'session_auth':
        from api.v1.auth.session_auth import SessionAuth
        auth = SessionAuth()


@app.before_request
def before_req():
    """Function to handle all request authorization"""
    # print('in before req')
    # print(f'Auth instance: {auth}')
    if auth is None:
        return
    # print(f'Request path: {request.path}')
    if not auth.require_auth(request.path, ['/api/v1/status/',
                                            '/api/v1/unauthorized/',
                                            '/api/v1/auth_session/login/',
                                            '/api/v1/forbidden/']):
        return
    auth_header = auth.authorization_header(request)
    if auth_header is None and auth.session_cookie(request) is None:
        abort(401)
    request.current_user = auth.current_user(request)
    if request.current_user is None:
        abort(403)

@app.route('/sessions', methods=['POST'])
def login():
    """Login function to respond to POST /sessions"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        abort(401)

    if not auth.valid_login(email, password):
        abort(401)

    user = auth.current_user(request)
    if user is None:
        abort(401)

    session_id = auth.create_session(user.id)
    response = make_response(jsonify({"message": "Logged in"}))
    response.set_cookie("session_id", session_id)
    return response

@app.errorhandler(401)
def not_authorized(error) -> str:
    """ Not authorized
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
