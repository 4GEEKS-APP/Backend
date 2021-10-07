from flask import Blueprint
from src.controllers.EventController import allEvents, createEvent, getById,deleteEvent,rateEvent, joinToEvent,unjoinToEvent,removeParticipant, addToFavorites, removeFromFavorites, postComment, getEventCategories, allEventsDetailed
from flask_jwt_extended import jwt_required

event_bp = Blueprint('event_bp', __name__)

event_bp.route('/', methods=['GET'])(allEvents) #ok
event_bp.route('/categories', methods=['GET'])(getEventCategories) #ok
event_bp.route('/detailed', methods=['GET'])(allEventsDetailed) #ok
event_bp.route('/create', methods=['POST'])(createEvent)#ok
event_bp.route('/<int:event_id>', methods=['GET'])(getById)#ok
event_bp.route('/<int:event_id>/edit', methods=['POST'])(deleteEvent)
event_bp.route('/<int:event_id>/rate', methods=['POST'])(rateEvent)
event_bp.route('/<int:event_id>/participant', methods=['POST'])(joinToEvent)#ok
event_bp.route('/<int:event_id>/participant', methods=['DELETE'])(unjoinToEvent)#ok
event_bp.route('/<int:event_id>/creator/participant', methods=['DELETE'])(removeParticipant)#ok
event_bp.route('/<int:event_id>/favorite', methods=['POST'])(addToFavorites)#ok
event_bp.route('/<int:event_id>/favorite', methods=['DELETE'])(removeFromFavorites)#ok
event_bp.route('/<int:event_id>/comment', methods=['POST'])(postComment)#ok



