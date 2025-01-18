from middleware.jwt_auth import token_required, admin_required
from service.item_service import create_item, get_item_paggination_service
from flask import request, jsonify

@token_required
def create_item_controller(current_user):
    if 'image' not in request.files:
        return jsonify({"error": "No image part in the request"}), 400

    image = request.files['image']

    response_data = create_item(request.form, image, current_user['id'])
    return response_data

@token_required
def get_item_paggination_controller(current_user):
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    response_data = get_item_paggination_service(page, limit)
    return response_data
