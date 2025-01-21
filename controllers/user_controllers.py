from flask import request
from middleware.jwt_auth import token_required, admin_required
from service.user_service import delete_user_by_admin_service, get_user_by_id_service, get_user_current_service, update_user_service, get_all_user_service, update_user_by_admin_service, update_user_by_admin_service

@token_required
def get_user_current_controller(current_user):
    response_data = get_user_current_service(current_user['id'])
    return response_data

@token_required
def update_user_controller(current_user):
    request_data = request.get_json()
    response_data = update_user_service(current_user['id'], request_data)
    return response_data

@admin_required
def get_all_user_controller(current_user):
    response_data = get_all_user_service()
    return response_data

@admin_required
def get_user_by_id_controller(current_user, user_id):
    response_data = get_user_by_id_service(user_id)
    return response_data
@admin_required
def update_user_by_admin_controller(current_user, user_id):
    request_data = request.get_json()
    response_data = update_user_by_admin_service(user_id, request_data)
    return response_data

@admin_required
def delete_user_by_admin_controller(current_user,user_id):
    response_data = delete_user_by_admin_service(user_id)
    return response_data