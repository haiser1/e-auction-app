from middleware.jwt_auth import admin_required
from flask import request
from service.auction_service import create_auction_service, delete_auction_service, get_auction_by_id_service, get_auction_pagination_service, update_auction_service

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

@admin_required
def get_auction_by_id_controller(current_user, auction_id):
    response_data = get_auction_by_id_service(auction_id)
    return response_data

@admin_required
def update_auction_controller(current_user, auction_id):
    request_data = request.get_json()
    response_data = update_auction_service(auction_id, request_data)
    return response_data

@admin_required
def delete_auction_controller(current_user, auction_id):
    response_data = delete_auction_service(auction_id)
    return response_data