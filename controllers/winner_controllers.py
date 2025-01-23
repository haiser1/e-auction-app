from service.winner_service import create_winner_service, get_all_winner_service, get_winner_by_user_service
from flask import request
from middleware.jwt_auth import admin_required, token_required

@admin_required
def create_winner_controller(current_user, auction_id):
    response_data = create_winner_service(auction_id)
    return response_data

@admin_required
def get_all_winner_controller(current_user):
    response_data = get_all_winner_service()
    return response_data

@token_required
def get_winner_by_user_controller(current_user):
    response_data = get_winner_by_user_service(current_user['id'])
    return response_data