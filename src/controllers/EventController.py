import sys
from flask import request, jsonify
from src.models.EventComment import EventComment
from src.models.User import User
from src.models.Event import Event
from src.models.EventRating import EventRating
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from src.models.Category import Category
import datetime

@jwt_required()
def allEvents():
    events = Event.query.all()
    serialized = list(map(lambda e: e.simple(),events))
    return jsonify(serialized)

@jwt_required()
def allEventsDetailed():
    events = Event.query.all()
    serialized = list(map(lambda e: e.serialize(),events))
    return jsonify(serialized)

@jwt_required()
def createEvent():
    data = request.get_json()
    if data.get('date_start') == None or data.get('category_id') == None or data.get('title') == None or data.get('description') == None:
        return jsonify({'message':'Bad request. You must provide date_start, category_id, title AND description.'}),400


    event = Event()
    event.title = data['title']
    event.description = data['description']
    event.gender = data['gender']
    event.level = data['level']
    event.max_members = data['max_members']
    event.thumbnail = data['thumbnail']
    event.category_id = data['category_id']
    event.date_start = data['date_start']
    current_user_id = get_jwt_identity()
    event.creator_id = current_user_id
    user = User.query.get(current_user_id)
    event.participants.append(user)
    event.created_at = datetime.datetime.utcnow()
    event.updated_at = datetime.datetime.utcnow()
    event.save()

    return jsonify(event.simple())
@jwt_required()
def getEventCategories():
    categories = Category.query.all()
    parsed = list(map(lambda c: c.serialize(), categories))

    return jsonify(parsed)

@jwt_required()
def getById(event_id):
    event = Event.query.get(event_id)
    if not event:
        return jsonify({'message': 'There is not event with this id'}),400

    return jsonify(event.serialize()),200

@jwt_required()
def rateEvent(event_id):
    event = Event.query.get(event_id)
    if not event:
        return jsonify({'message': 'There is not event with this id'}),400
    request_data = request.get_json()
    current_user_id = get_jwt_identity()

    rating = EventRating()
    rating.created_at = datetime.utcnow()
    rating.user_id = current_user_id
    rating.category = 'one'
    rating.event_id = event.id
    rating.value = request_data['value']

    rating.save()

    return jsonify({'message': 'Success', 'rating': rating.serialize()})

@jwt_required()
def updateEvent(event_id):
    return 'Update an event'

@jwt_required()
def deleteEvent(event_id):
    return 'Delete an event'

@jwt_required()
def joinToEvent(event_id):
    event = Event.query.get(event_id)
    if event == None:
        return jsonify({'message':'There is not event with provided id'})
    current_user_id = get_jwt_identity()
    participant = User.query.get(current_user_id)
    event.participants.append(participant)

    event.save()
    return jsonify({'message':'Success. The user was joined to event.', 'event': event.serialize()})

@jwt_required()
def unjoinToEvent(event_id):
    event = Event.query.get(event_id)
    if event == None:
        return jsonify({'message':'There is not event with provided id.'})

    current_user_id = get_jwt_identity()
    participant = User.query.get(current_user_id)
    event.participants.remove(participant)
    event.save()
    return jsonify({'message':'Success. The user was removed from the event.', 'event': event.serialize()})

@jwt_required()
def removeParticipant(event_id):
    event = Event.query.get(event_id)
    if event == None:
        return jsonify({'message':'There is not event with provided id.'})

    current_user_id = get_jwt_identity()
    if event.creator_id == current_user_id:
        data = request.get_json()
        participant = User.query.get(data['user_id'])
        event.participants.remove(participant)
        event.save()
        return jsonify({'message':'Success. The user was removed from the event.', 'event': event.serialize()})

@jwt_required()
def addToFavorites(event_id):
    event = Event.query.get(event_id)
    if event == None:
        return jsonify({'message':'There is not event with provided id.'})
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    is_in_favorites = list(filter(lambda e: event == e, user.favorites))
    if len(is_in_favorites) > 0:
        return jsonify({'message':'The event is already in favorites list'})
    if len(is_in_favorites) == 0:
        user.favorites.append(event)
        user.save()
        favorites = list(map(lambda event: event.simple(), user.favorites))
        return jsonify({'message':'Success. The event was added to favorites list.', 'favorites': favorites})

@jwt_required()
def removeFromFavorites(event_id):
    event = Event.query.get(event_id)
    if event == None:
        return jsonify({'message':'There is not event with provided id.'})

    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    is_in_favorites = list(filter(lambda e: event == e, user.favorites))

    if len(is_in_favorites) > 0:
        user.favorites.remove(event)
    if len(is_in_favorites) == 0:
        return jsonify({'message':'There is not favorite events with provided id in user list.'})
    user.save()
    favorites = list(map(lambda event: event.simple(), user.favorites))
    return jsonify({'message':'Success. Event was removed from favorites list.', 'favorites': favorites})

@jwt_required()
def postComment(event_id):
    event = Event.query.get(event_id)
    if event == None:
        return jsonify({'message':'There is not event with provided id'})
    
    data = request.get_json()
    current_user_id = get_jwt_identity()
    comment = EventComment(
        created_at = datetime.datetime.utcnow(),
        updated_at = datetime.datetime.utcnow(),
        user_id = current_user_id,
        event_id = event.id,
        body = data['body']     
    )

    comment.save()
    return jsonify({'message':'Success'})
    
