from flask import Blueprint
from controllers.EventController import allEvents, createEvent, getById,deleteEvent,rateEvent, uploadImg,

event_bp = Blueprint('event_bp', __name__)

event_bp.route('/', methods=['GET'])(allEvents)
event_bp.route('/create', methods=['POST'])(createEvent)
event_bp.route('/<int:event_id>', methods=['GET'])(getById)
event_bp.route('/<int:event_id>/edit', methods=['POST'])(deleteEvent)
event_bp.route('/<int:event_id>/rate', methods=['POST'])(rateEvent)

event_bp.route('/<int:event_id>/upload', methods=['POST'])(uploadImg)