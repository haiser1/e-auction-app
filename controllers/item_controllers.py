from middleware.jwt_auth import token_required, admin_required
from service.item_service import (
    create_item, get_item_by_id_service,
    get_item_by_user_pagination_service,
    update_item_by_user_service, 
    delete_item_by_user_service,
    get_item_by_admin_pagination_service
    )
from flask import request, jsonify

@token_required
def create_item_controller(current_user):
    if 'image' not in request.files:
        return jsonify({"error": "No image part in the request"}), 400

    image = request.files['image']

    response_data = create_item(request.form, image, current_user['id'])
    return response_data

@token_required
def get_item_by_user_pagination_controller(current_user):
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    response_data = get_item_by_user_pagination_service(page, limit, current_user['id'])
    return response_data

@token_required
def get_item_by_id_controller(current_user, item_id):
    response_data = get_item_by_id_service(item_id, current_user['id'])
    return response_data

@token_required
def update_item_by_user_controller(current_user, item_id):
    if 'image' not in request.files:
        image = None
    else:
        image = request.files['image']

    response_data = update_item_by_user_service(item_id, request.form, current_user['id'], image)
    return response_data

@token_required
def delete_item_by_user_controller(current_user, item_id):
    response_data = delete_item_by_user_service(item_id, current_user['id'])
    return response_data

@admin_required
def get_item_by_admin_pagination_controller(current_user):
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    response_data = get_item_by_admin_pagination_service(page, limit)
    return response_data
