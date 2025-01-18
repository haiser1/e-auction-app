import logging
from models.item import Item
from vallidation.item_validation import CreateItemValidation
from helper.upload_to_cloudinary import upload_to_cloudinary
from base_response.base_response import BaseResponse
from flask import jsonify
from config import db
from marshmallow import ValidationError

def create_item(request_data, image, user_id):
    try:
        data = CreateItemValidation().load(request_data)
        find = Item.query.filter_by(name=data['name'],user_id=user_id, deleted_at=None).first()
        if find is not None:
            return jsonify(BaseResponse.response_error('Item already exists')), 400
        if image is None:
            return jsonify(BaseResponse.response_error('Image is required')), 400

        if not image.content_type.startswith("image/"):
            return jsonify(BaseResponse.response_error("Invalid file type. Please upload an image.")), 400

        if image.content_length > 3 * 1024 * 1024:
            return jsonify(BaseResponse.response_error("File size exceeds 5MB. Please upload a smaller file.")), 400
        image_url = upload_to_cloudinary(image.stream)
        if image_url is None:
            return jsonify(BaseResponse.response_error("Failed to upload image")), 500
        data_item = Item(name=data['name'],description=data['description'], image_url=image_url, starting_price=data['starting_price'], user_id=user_id, status='open')
        db.session.add(data_item)
        db.session.commit()
        return jsonify(BaseResponse.response_success(data_item.to_dict())), 201
    
    except ValidationError as e:
        return jsonify(BaseResponse.response_error(e.messages)), 400
    
    except Exception as ex:
        logging.error(ex)
        return jsonify(BaseResponse.response_error('Internal server error')), 500

