from flask import Blueprint
from controllers.item_controllers import create_item_controller, get_item_by_user_pagination_controller, get_item_by_id_controller

item_route = Blueprint('item_route', __name__)

item_route.post('/api/users/items')(create_item_controller)
item_route.get('/api/users/me/items')(get_item_by_user_pagination_controller)
item_route.get('/api/users/items/<int:item_id>')(get_item_by_id_controller)