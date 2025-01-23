from controllers.winner_controllers import create_winner_controller, get_all_winner_controller, get_winner_by_user_controller
from flask import Blueprint

winner_route = Blueprint('winner_route', __name__)

winner_route.post('/api/auctions/<int:auction_id>/winners')(create_winner_controller)
winner_route.get('/api/admin/winners')(get_all_winner_controller)
winner_route.get('/api/users/me/winners')(get_winner_by_user_controller)