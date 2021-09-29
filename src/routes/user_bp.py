from flask import Blueprint
from controllers.UserController import index, store, show, update, destroy, follow, unfollow
user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(index)
user_bp.route('/create', methods=['POST'])(store)
user_bp.route('/<int:user_id>', methods=['GET'])(show)
user_bp.route('/<int:user_id>/update', methods=['PUT'])(update)
user_bp.route('/<int:target_id>/follow', methods=['POST'])(follow)
user_bp.route('/<int:target_id>/unfollow', methods=['POST'])(unfollow)
