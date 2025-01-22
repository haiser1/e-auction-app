from middleware.jwt_auth import admin_required
from flask import request
from service.auction_service import create_auction_service, get_auction_pagination_service

@admin_required
def create_auction_controller(current_user):
    request_data = request.get_json()
    response_data = create_auction_service(request_data)
    return response_data

@admin_required
def get_auction_pagination_controller(current_user):
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    response_data = get_auction_pagination_service(page, limit)
    return response_data