from flask import Blueprint
from controllers.EventController import allEvents, createEvent, getById,deleteEvent,rateEvent, joinToEvent,unjoinToEvent,removeParticipant, addToFavorites, removeFromFavorites, postComment
from flask_jwt_extended import jwt_required

event_bp = Blueprint('event_bp', __name__)

event_bp.route('/', methods=['GET'])(allEvents)
event_bp.route('/create', methods=['POST'])(createEvent)
event_bp.route('/<int:event_id>', methods=['GET'])(getById)
event_bp.route('/<int:event_id>/edit', methods=['POST'])(deleteEvent)
event_bp.route('/<int:event_id>/rate', methods=['POST'])(rateEvent)
event_bp.route('/<int:event_id>/participant', methods=['POST'])(joinToEvent)
event_bp.route('/<int:event_id>/participant', methods=['DELETE'])(unjoinToEvent)
event_bp.route('/<int:event_id>/creator/participant', methods=['DELETE'])(removeParticipant)
event_bp.route('/<int:event_id>/favorite', methods=['POST'])(addToFavorites)
event_bp.route('/<int:event_id>/favorite', methods=['DELETE'])(removeFromFavorites)
event_bp.route('/<int:event_id>/comment', methods=['POST'])(postComment)



