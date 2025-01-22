from flask import Blueprint
from controllers.bid_controlers import create_bid_controller

bid_route = Blueprint('bid_route', __name__)

bid_route.post('/api/auctions/<int:auction_id>/bids')(create_bid_controller)