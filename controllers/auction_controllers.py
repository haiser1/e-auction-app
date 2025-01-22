from middleware.jwt_auth import admin_required
from flask import request
from service.auction_service import create_auction_service

@admin_required
def create_auction_controller(current_user):
    request_data = request.get_json()
    response_data = create_auction_service(request_data)
    return response_data