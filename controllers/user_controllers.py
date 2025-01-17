from flask import request
from middleware.jwt_auth import token_required
from service.user_service import get_user_current_service, update_user_service

@token_required
def get_user_current_controller(current_user):
    response_data = get_user_current_service(current_user['id'])
    return response_data

@token_required
def update_user_controller(current_user):
    request_data = request.get_json()
    response_data = update_user_service(current_user['id'], request_data)
    return response_data