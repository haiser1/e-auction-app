from flask import Blueprint
from controllers.user_controllers import get_user_by_id_controller, get_user_current_controller, update_user_controller, get_all_user_controller, update_user_by_admin_controller, delete_user_by_admin_controller

user_route = Blueprint('user_route', __name__)

user_route.get('/api/users/me')(get_user_current_controller)
user_route.patch('/api/users/me')(update_user_controller)
user_route.get('/api/users')(get_all_user_controller)
user_route.get('/api/users/<int:user_id>')(get_user_by_id_controller)
user_route.patch('/api/admin/users/<int:user_id>')(update_user_by_admin_controller)
user_route.delete('/api/admin/users/<int:user_id>')(delete_user_by_admin_controller)