from flask import Blueprint
from controllers.item_controllers import create_item_controller, get_item_paggination_controller

item_route = Blueprint('item_route', __name__)

item_route.post('/api/user/items')(create_item_controller)
item_route.get('/api/user/items')(get_item_paggination_controller)