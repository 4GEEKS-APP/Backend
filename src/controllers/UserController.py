import sys
from flask import request
from src.models.User import User
from flask import jsonify
from flask_jwt_extended import create_access_token,get_jwt_identity
from flask_bcrypt import generate_password_hash, check_password_hash
import datetime
from src.models.UserRole import UserRole
from flask_jwt_extended import jwt_required
from datetime import timedelta


def login():
    request_data = request.get_json()
    user = User.query.filter_by(email=request_data['email']).first()
    if user == None:
        return jsonify({'message':'Unauthorized, bad credentials.'}),401
    
    if check_password_hash(user.password, request_data['password']):
        expires = timedelta(days=1)
        acces_token = create_access_token(identity=user.id, expires_delta=expires)
        return jsonify({'message': 'Login succes!', 'user': user.serialize(), 'token': acces_token})
    else:
        return jsonify({'message':'Unauthorized, bad credentials.'}),401

def index():
    users = User.query.all()
    serialized = list(map(lambda u: u.serialize(), users))
    return jsonify({'message':'Success', 'users': serialized})

def tokenDecode():
    current_user_id = get_jwt_identity()
    return jsonify(user_id=current_user_id), 200

def register():
    request_data = request.get_json()

    if request_data.get('email') == None or request_data.get('full_name') == None or request_data.get('password') == None or request_data.get('gender') == None:
        return jsonify({'message':'Bad request. You must provide email, password, full_name and gender.'}),400

    user = User.query.filter_by(email = request_data['email']).first()
    if user is not None:
        return jsonify({'message':'The email provided is already associated with another account'}),400

        
    roleUser = UserRole.query.filter_by(title='User').first()
    serialized = roleUser.serialize()
    newUser = User()
    newUser.email = request_data['email']
    newUser.full_name = request_data['full_name']
    newUser.role_id = serialized['id']
    newUser.gender = request_data['gender']
    newUser.created_at = datetime.datetime.utcnow()
    newUser.updated_at = datetime.datetime.utcnow()
    newUser.password = generate_password_hash(request_data['password'], 10).decode('utf-8')
    newUser.save()
    return jsonify({'message':'Success, user registered', 'user': newUser.serialize()})

def admin_register():
    request_data = request.get_json()

    newUser = User()
    newUser.email = request_data['email']
    newUser.full_name = request_data['full_name']
    newUser.role_id = 1
    newUser.created_at = datetime.datetime.utcnow()
    newUser.updated_at = datetime.datetime.utcnow()
    newUser.password = generate_password_hash(request_data['password'], 10).decode('utf-8')
    newUser.save()
    return jsonify({'message':'Success, user registered', 'user': newUser.serialize()})
    
@jwt_required()
def follow(target_id):
    user = User.query.get(target_id)
    if not user:
        return jsonify({'message': 'There is not user with provided id!'}),400
    current_user_id = get_jwt_identity()
    follower = User.query.get(current_user_id)
 
    user.followers.append(follower)
    user.save()

    return jsonify({'message':'Success follow'})

@jwt_required()
def unfollow(target_id):
    user = User.query.get(target_id)
    if not user:
        return jsonify({'message': 'There is not user with provided id!'}),400
    current_user_id = get_jwt_identity()
    follower = User.query.get(current_user_id)
    
    user.followers.remove(follower)
    user.save()

    return jsonify({'message':'Success unfollow'})

def show(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message':'There is not user with provided id'})
    return jsonify(user.serialize())

def update(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if(data == None):
        return jsonify({'message': 'Bad request. You must provide at least one editable property'}),400
    has_full_name = "full_name" in data
    has_avatar_url = "avatar_url" in data

    if(has_avatar_url):
        user.avatar_url = data['avatar_url']
    user.save()
    return jsonify({'message': 'Success', 'user':user.serialize()})


def destroy(user_id):
    return 'Delete an user'