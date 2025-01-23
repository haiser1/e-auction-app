from service.winner_service import create_winner_service
from flask import request
from middleware.jwt_auth import admin_required

@admin_required
def create_winner_controller(current_user, auction_id):
    response_data = create_winner_service(auction_id)
    return response_data