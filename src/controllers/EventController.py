import sys
from flask import request
from flask import jsonify
from models.Event import Event
from models.EventRating import EventRating
from datetime import datetime


def allEvents():
    events = Event.query.all()
    serialized = list(map(lambda e: e.serialize(),events))
    return jsonify(serialized)
def createEvent():
    # Capture request body
    data = request.get_json()
    # Create a new event instance
    event = Event()

    # Populate new event instance
    event.title = data['title']
    event.description = data['description']
    event.creator = 1
    event.created_at = datetime.utcnow()
    event.updated_at = datetime.utcnow()
    # Save new Instance
    event.save()
    # Return new saved instance
    return jsonify(event.serialize())

def getById(event_id):
    event = Event.query.get(event_id)
    if not event:
        return jsonify({'message': 'There is not event with this id'}),400

    return jsonify(event.serialize()),200

def rateEvent(event_id):
    event = Event.query.get(event_id)
    if not event:
        return jsonify({'message': 'There is not event with this id'}),400
    # Capture request body
    request_data = request.get_json()

    rating = EventRating()
    rating.created_at = datetime.utcnow()
    rating.user_id = 4
    rating.category = 'one'
    rating.event_id = event.id
    rating.value = 5

    rating.save()

    return jsonify({'message': 'Success', 'rating': rating.serialize()})

def updateEvent(event_id):
    return 'Update an event'
def deleteEvent(event_id):
    return 'Delete an event'
#Desde aqui#
def uploadImg(event_id):
    event = Event.query.get(event_id)
    if event == None:
         return jsonify({'message':'No existe el evento'})

         data = request.get_json()

         if data['img_url'] == None:
             return jsonify({'massage':'Fail'}),400

         img = EventImage()
         img.event_id = event_id
         img.img_url = data['img_url']

         img.save()

         return jsonify({'message':'Success', 'event':event, 'event_img': img})