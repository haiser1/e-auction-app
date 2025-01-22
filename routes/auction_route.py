from flask import Blueprint
from controllers.auction_controllers import (
    create_auction_controller,
    get_auction_pagination_controller,
    get_auction_by_id_controller
    )

auction_route = Blueprint('auction_route', __name__)

auction_route.post('/api/auctions')(create_auction_controller)
auction_route.get('/api/auctions')(get_auction_pagination_controller)
auction_route.get('/api/auctions/<int:auction_id>')(get_auction_by_id_controller)