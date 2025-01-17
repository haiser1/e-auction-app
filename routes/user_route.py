from flask import Blueprint
from controllers.user_controllers import get_user_current_controller

user_route = Blueprint('user_route', __name__)

user_route.get('/api/user')(get_user_current_controller)