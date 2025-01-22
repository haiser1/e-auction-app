from service.bid_service import create_bid_service
from flask import request
from middleware.jwt_auth import token_required

@token_required
def create_bid_controller(current_user, auction_id):
    request_data = request.get_json()
    response_data = create_bid_service(request_data, auction_id, current_user['id'])
    return response_data