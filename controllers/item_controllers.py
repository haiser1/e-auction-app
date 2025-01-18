from middleware.jwt_auth import token_required, admin_required
from service.item_service import create_item
from flask import request, jsonify

@token_required
def create_item_controller(current_user):
    if 'image' not in request.files:
        return jsonify({"error": "No image part in the request"}), 400

    image = request.files['image']

    response_data = create_item(request.form, image, current_user['id'])
    return response_data
