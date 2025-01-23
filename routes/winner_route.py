from controllers.winner_controllers import create_winner_controller
from flask import Blueprint

winner_route = Blueprint('winner_route', __name__)

winner_route.post('/api/auctions/<int:auction_id>/winners')(create_winner_controller)