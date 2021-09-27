import sys
""" from flask import render_template, redirect, url_for, request, abort """
from models.User import User
from flask import jsonify


def index():
    return 'Return all users'
def store():
    return 'Create a new user'



def show(user_id):
    return jsonify({"id": user_id})




def update(user_id):
    return 'Update an user'
def destroy(user_id):
    return 'Delete an user'