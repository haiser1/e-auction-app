from flask import Blueprint
from controllers.auth_controller import register_controller, login_controller

auth_route = Blueprint('auth_route', __name__)

auth_route.post('/api/register')(register_controller)
auth_route.post('/api/login')(login_controller)