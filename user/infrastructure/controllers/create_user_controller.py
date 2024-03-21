from flask import Blueprint, request, jsonify
from user.application.usecases.register_user import RegisterUser
from user.infrastructure.repositories.user_repository import MongoDBUserRepository

create_user_blueprint = Blueprint('create_user', __name__)

def initialize_endpoints(repository):
    register_user_usecase = RegisterUser(user_repository=repository)

    @create_user_blueprint.route('/register', methods=['POST'])
    def register_user():
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        try:
            register_user_usecase.execute(name, email, password)
            return jsonify({"message": "User registered successfully"}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
