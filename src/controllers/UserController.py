import sys
from flask import request
from models.User import User
from flask import jsonify


def index():
    users = User.query.all()
    serialized = list(map(lambda u: u.serialize(), users))

    return jsonify({'message':'Success', 'users': serialized})
def store():
    return 'Create a new user'

def follow(target_id):
    user = User.query.get(target_id)
    follower = User.query.get(2)
    if not user:
        return jsonify({'message': 'There is not user with provided id!'}),400
 
    user.followers.append(follower)
    user.save()

    return jsonify({'message':'Success follow'})

def unfollow(target_id):
    user = User.query.get(target_id)
    follower = User.query.get(2)
    if not user:
        return jsonify({'message': 'There is not user with provided id!'}),400
    
    user.followers.remove(follower)
    user.save()

    return jsonify({'message':'Success unfollow'})


def show(user_id):
    user = User.query.get(user_id)
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