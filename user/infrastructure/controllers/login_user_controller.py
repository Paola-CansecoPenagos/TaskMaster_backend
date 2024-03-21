from flask import Blueprint, request, jsonify
from user.application.usecases.login_user import LoginUser
from user.infrastructure.repositories.user_repository import MongoDBUserRepository

login_user_blueprint = Blueprint('login_user', __name__)

def initialize_endpoints(repository):
    login_user_usecase = LoginUser(user_repository=repository)

    @login_user_blueprint.route('/login', methods=['POST'])
    def login_user():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = login_user_usecase.execute(email, password)
        if user:
            return jsonify({"message": "Login successful", "user": user.name}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401