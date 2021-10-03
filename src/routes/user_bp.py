from flask import Blueprint
from src.controllers.UserController import index, register, show, update, follow, unfollow, login, admin_register, tokenDecode
from flask_jwt_extended import jwt_required

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(index)    
user_bp.route('/login', methods=['POST'])(login)
user_bp.route('/register', methods=['POST'])(register)
user_bp.route('/<int:user_id>', methods=['GET'])(show)
user_bp.route('/<int:user_id>/update', methods=['PUT'])(update)
user_bp.route('/<int:target_id>/follow', methods=['POST'])(follow)
user_bp.route('/<int:target_id>/unfollow', methods=['POST'])(unfollow)

#Especial endpoint
user_bp.route('/admin/register', methods=['POST'])(admin_register)