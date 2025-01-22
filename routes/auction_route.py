from flask import Blueprint
from controllers.auction_controllers import create_auction_controller

auction_route = Blueprint('auction_route', __name__)

auction_route.post('/api/auctions')(create_auction_controller)