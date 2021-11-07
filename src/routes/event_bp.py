from flask import Blueprint
<<<<<<< HEAD
from src.controllers.EventController import allEvents, createEvent, getById,deleteEvent,rateEvent, joinToEvent,unjoinToEvent,removeParticipant, addToFavorites, removeFromFavorites, postComment, getEventCategories, allEventsDetailed, addEventMedia
from flask_jwt_extended import jwt_required
=======
from controllers.EventController import allEvents, createEvent, getById,deleteEvent,rateEvent, uploadImg,
>>>>>>> 2ee1fa37dca97e9e854274d4e0df6094a036c226

event_bp = Blueprint('event_bp', __name__)

event_bp.route('/', methods=['GET'])(allEvents)
event_bp.route('/categories', methods=['GET'])(getEventCategories)
event_bp.route('/detailed', methods=['GET'])(allEventsDetailed)
event_bp.route('/create', methods=['POST'])(createEvent)
event_bp.route('/<int:event_id>', methods=['GET'])(getById)
event_bp.route('/<int:event_id>/edit', methods=['POST'])(deleteEvent)
event_bp.route('/<int:event_id>/rate', methods=['POST'])(rateEvent)
<<<<<<< HEAD
event_bp.route('/<int:event_id>/creator/participant', methods=['DELETE'])(removeParticipant)
event_bp.route('/<int:event_id>/participant', methods=['POST'])(joinToEvent)
event_bp.route('/<int:event_id>/participant', methods=['DELETE'])(unjoinToEvent)
event_bp.route('/<int:event_id>/favorite', methods=['POST'])(addToFavorites)
event_bp.route('/<int:event_id>/favorite', methods=['DELETE'])(removeFromFavorites)
event_bp.route('/<int:event_id>/comment', methods=['POST'])(postComment)
event_bp.route('/<int:event_id>/media', methods=['POST'])(addEventMedia)



=======

event_bp.route('/<int:event_id>/upload', methods=['POST'])(uploadImg)
>>>>>>> 2ee1fa37dca97e9e854274d4e0df6094a036c226
